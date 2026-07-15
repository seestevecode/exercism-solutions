defmodule Plot do
  @enforce_keys [:plot_id, :registered_to]
  defstruct [:plot_id, :registered_to]
end

defmodule CommunityGarden do
  def start(opts \\ []), do: Agent.start(fn -> %{plots: [], next_id: 1} end, opts)

  def list_registrations(pid), do: Agent.get(pid, fn state -> state.plots end)

  def register(pid, register_to), do:
    Agent.get_and_update(pid, fn state ->
      plot = %Plot{plot_id: state.next_id, registered_to: register_to}
      new_state = %{plots: state.plots ++ [plot], next_id: state.next_id + 1}
      {plot, new_state}
    end)

  def release(pid, plot_id), do:
    Agent.update(pid, fn state ->
      remaining_plots = Enum.reject(state.plots, fn plot -> plot.plot_id == plot_id end)
      %{state | plots: remaining_plots}
    end)

  def get_registration(pid, plot_id), do:
    Agent.get(pid, fn state ->
      case Enum.find(state.plots, fn plot -> plot.plot_id == plot_id end) do
        nil -> {:not_found, "plot is unregistered"}
        plot -> plot
      end
    end)
end
