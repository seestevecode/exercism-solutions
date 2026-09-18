defmodule Anagram do
  @doc """
  Returns all candidates that are anagrams of, but not equal to, 'base'.
  """
  @spec match(String.t(), [String.t()]) :: [String.t()]
  def match(base, candidates), do:
    Enum.filter(
      candidates,
      fn candidate -> 
        sort_lower(candidate) == sort_lower(base) 
          and String.downcase(candidate) != String.downcase(base) 
      end)

  defp sort_lower(string), do:
    string |> String.downcase() |> String.graphemes() |> Enum.sort() |> Enum.join()
end
