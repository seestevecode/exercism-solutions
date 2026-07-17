defmodule RPNCalculatorInspection do
  def start_reliability_check(calculator, input) do
    %{input: input, pid: spawn_link(fn -> calculator.(input) end)}
  end

  def await_reliability_check_result(%{pid: pid, input: input}, results) do
    receive do
      {:EXIT, ^pid, :normal} -> Map.put(results, input, :ok)
      {:EXIT, ^pid, _reason} -> Map.put(results, input, :error)
    after
      100 -> Map.put(results, input, :timeout)
    end
  end

  def reliability_check(calculator, inputs) do
    old_flag = Process.flag(:trap_exit, true)
    checks = Enum.map(inputs, fn input ->
      start_reliability_check(calculator, input)
      end)
    results = Enum.reduce(checks, %{}, fn check, results ->
      await_reliability_check_result(check, results)
      end)
    Process.flag(:trap_exit, old_flag)
    results
  end

  def correctness_check(calculator, inputs) do
    tasks = Enum.map(inputs, fn input ->
      Task.async(fn -> calculator.(input) end) end)
    Enum.map(tasks, fn task -> Task.await(task, 100) end)
  end
end
