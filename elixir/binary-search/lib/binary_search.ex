defmodule BinarySearch do
  @doc """
    Searches for a key in the tuple using the binary search algorithm.
    It returns :not_found if the key is not in the tuple.
    Otherwise returns {:ok, index}.

    ## Examples

      iex> BinarySearch.search({}, 2)
      :not_found

      iex> BinarySearch.search({1, 3, 5}, 2)
      :not_found

      iex> BinarySearch.search({1, 3, 5}, 5)
      {:ok, 2}

  """

  @spec search(tuple, integer) :: {:ok, integer} | :not_found
  def search({}, _key), do: :not_found
  def search(numbers, key), do: 
    numbers 
    |> Tuple.to_list() 
    |> Enum.sort() 
    |> List.to_tuple() 
    |> do_search(key, 0, tuple_size(numbers) - 1)

  defp do_search(_numbers, _key, min, max) when min > max, do: :not_found
  defp do_search(numbers, key, min, max) do
    mid = div(min + max, 2)
    value = elem(numbers, mid)
    cond do
      value == key -> {:ok, mid}
      value < key -> do_search(numbers, key, mid + 1, max)
      value > key -> do_search(numbers, key, min, mid - 1)
    end
  end
end
