defmodule PaintByNumber do
  def palette_bit_size(color_count), do: get_bit_size(color_count, 1)

  defp get_bit_size(color_count, count), do:
    if 2 ** count >= color_count, do: count, else: get_bit_size(color_count, count + 1)

  def empty_picture(), do: <<>>

  def test_picture(), do: <<0::2, 1::2, 2::2, 3::2>>

  def prepend_pixel(picture, color_count, pixel_color_index) do
    bit_size = palette_bit_size(color_count)
    <<pixel_color_index::size(bit_size), picture::bitstring>>
  end

  def get_first_pixel(picture, color_count), do: split_picture(picture, color_count) |> elem(0)

  def drop_first_pixel(picture, color_count), do: split_picture(picture, color_count) |> elem(1)

  defp split_picture(<<>>, _color_count), do: {nil, ""}
  defp split_picture(picture, color_count) do
    bit_size = palette_bit_size(color_count)
    <<pixel::size(bit_size), rest::bitstring>> = picture
    {pixel, rest}
  end

  def concat_pictures(picture1, picture2), do: <<picture1::bitstring, picture2::bitstring>>
end
