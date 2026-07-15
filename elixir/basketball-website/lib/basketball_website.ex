defmodule BasketballWebsite do
  def extract_from_path(data, path), do: 
    do_extract_from_path(data, String.split(path, "."))

  defp do_extract_from_path(data, []), do: data
  defp do_extract_from_path(data, [first | rest]), do:
    do_extract_from_path(data[first], rest)
    
  def get_in_path(data, path), do: get_in(data, String.split(path, "."))
end
