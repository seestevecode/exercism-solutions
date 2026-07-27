defmodule MatchingBrackets do
  @pairs %{?[ => ?], ?( => ?), ?{ => ?}}
  @opening_brackets Map.keys(@pairs)
  @closing_brackets Map.values(@pairs)

  @doc """
  Checks that all the brackets and braces in the string are matched correctly, and nested correctly
  """
  @spec check_brackets(String.t()) :: boolean
  def check_brackets(str) do
    str
    |> String.to_charlist()
    |> Enum.reduce_while([], fn
      # always push an opening bracket to the stack
      bracket, stack when bracket in @opening_brackets -> {:cont, [bracket | stack]}

      # if a closing bracket and non-empty stack, 
      # continue with rest if it pairs with top, else halt
      bracket, [top | rest] when bracket in @closing_brackets ->
        if bracket == @pairs[top], do: {:cont, rest}, else: {:halt, :invalid}

      # cannot push a closing bracket to an empty stack, so halt
      bracket, [] when bracket in @closing_brackets -> {:halt, :invalid}

      # any other character should be ignored, continuing with the stack as-is
      _character, stack -> {:cont, stack}
    end)
    |> Kernel.==([])
  end
end
