defmodule SpaceAge do
  @type planet ::
          :mercury
          | :venus
          | :earth
          | :mars
          | :jupiter
          | :saturn
          | :uranus
          | :neptune

  @earth_year_in_seconds 31557600

  @doc """
  Return the number of years a person that has lived for 'seconds' seconds is
  aged on 'planet', or an error if 'planet' is not a planet.
  """
  @spec age_on(planet, pos_integer) :: {:ok, float} | {:error, String.t()}
  def age_on(planet, seconds) do
    age_in_years = seconds / @earth_year_in_seconds
    case planet do
      :mercury -> {:ok, age_in_years / 0.2408467}
      :venus -> {:ok, age_in_years / 0.61519726}
      :earth -> {:ok, age_in_years / 1.0}
      :mars -> {:ok, age_in_years / 1.8808158}
      :jupiter -> {:ok, age_in_years / 11.862615}
      :saturn -> {:ok, age_in_years / 29.447498}
      :uranus -> {:ok, age_in_years / 84.016846}
      :neptune -> {:ok, age_in_years / 164.79132}
      _ -> {:error, "not a planet"}
    end
  end
end
