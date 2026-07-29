defmodule TopSecret do
  def to_ast(string), do: Code.string_to_quoted!(string)

  def decode_secret_message_part(
        {definition, _, [head, _body]} = ast,
        acc
      ) when definition in [:def, :defp] do
    {name, arguments} = function_head(head)
    arity = arguments |> List.wrap() |> length()
    part = name |> Atom.to_string() |> String.slice(0, arity)
    {ast, [part | acc]}
  end
  def decode_secret_message_part(ast, acc), do: {ast, acc}

  def decode_secret_message(string) do
    {_, parts} =
      string
      |> to_ast()
      |> Macro.prewalk([], &decode_secret_message_part/2)
    parts |> Enum.reverse() |> Enum.join()
  end

  defp function_head({:when, _, [head | _guards]}), do: function_head(head)
  defp function_head({name, _, arguments}), do: {name, arguments}
end
