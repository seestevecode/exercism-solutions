defmodule House do
  @doc """
  Return verses of the nursery rhyme 'This is the House that Jack Built'.
  """

  @noun_verbs %{
    2 => {"malt", "lay in"},
    3 => {"rat", "ate"},
    4 => {"cat", "killed"},
    5 => {"dog", "worried"},
    6 => {"cow with the crumpled horn", "tossed"},
    7 => {"maiden all forlorn", "milked"},
    8 => {"man all tattered and torn", "kissed"},
    9 => {"priest all shaven and shorn", "married"},
    10 => {"rooster that crowed in the morn", "woke"},
    11 => {"farmer sowing his corn", "kept"},
    12 => {"horse and the hound and the horn", "belonged to"}
  }
             
  @spec recite(start :: integer, stop :: integer) :: String.t()
  def recite(start, stop), do:
    start..stop |> Enum.map(&recite_verse/1) |> Enum.join()

  defp recite_verse(1), do: "This is the house that Jack built.\n"
  defp recite_verse(num) when num >= 2 and num <= 12, do:
    "This is " <>
      Enum.reduce(2..num, "", fn i, acc ->
        {noun, verb} = @noun_verbs[i]
        "the #{noun} that #{verb} " <> acc
      end) <>
      "the house that Jack built.\n"
end
