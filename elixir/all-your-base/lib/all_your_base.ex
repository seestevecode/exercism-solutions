defmodule AllYourBase do
  @doc """
  Given a number in input base, represented as a sequence of digits, converts it to output base,
  or returns an error tuple if either of the bases are less than 2
  """

  @spec convert(list, integer, integer) :: {:ok, list} | {:error, String.t()}
  def convert(_digits, input_base, _output_base) when input_base < 2, do:
    {:error, "input base must be >= 2"}
  def convert(_digits, _input_base, output_base) when output_base < 2, do:
    {:error, "output base must be >= 2"}
  def convert(digits, input_base, output_base) do
    if Enum.any?(digits, fn 
      digit -> not is_integer(digit) or digit < 0 or digit >= input_base 
    end) do
      {:error, "all digits must be >= 0 and < input base"}
    else
      digits |> from_digits(input_base) |> to_digits(output_base) |> then(&{:ok, &1})
    end
  end

  defp from_digits(digits, base), do:
    Enum.reduce(digits, 0, fn digit, acc -> base * acc + digit end)

  defp to_digits(0, _base), do: [0]
  defp to_digits(number, base), do: do_to_digits(number, base, [])

  defp do_to_digits(0, _base, result), do: result
  defp do_to_digits(number, base, result), do:
    do_to_digits(div(number, base), base, [rem(number, base) | result])
end
