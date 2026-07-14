defmodule Username do
  def sanitize([]), do: []
  def sanitize([head | tail]) do
    cleaned = case head do
      ?ä -> ~c"ae"
      ?ö -> ~c"oe"
      ?ü -> ~c"ue"
      ?ß -> ~c"ss"
      ch when (ch >= ?a and ch <= ?z) -> [ch]
      ?_ -> ~c"_"
      _ -> ~c""
    end
    cleaned ++ sanitize(tail)
  end
end
