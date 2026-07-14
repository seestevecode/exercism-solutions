defmodule Username do
  def sanitize([]), do: []
  def sanitize([head | tail]) do
    cleaned = case head do
      ?ä -> 'ae'
      ?ö -> 'oe'
      ?ü -> 'ue'
      ?ß -> 'ss'
      ch when (ch >= ?a and ch <= ?z) -> [ch]
      ?_ -> '_'
      _ -> ''
    end
    cleaned ++ sanitize(tail)
  end
end
