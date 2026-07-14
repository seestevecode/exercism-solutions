defmodule FreelancerRates do
  def daily_rate(hourly_rate) do
    hourly_rate * 8.0
  end

  def apply_discount(before_discount, discount) do
    before_discount * (1 - discount / 100)
  end

  def monthly_rate(hourly_rate, discount) do
    before_discount = daily_rate(hourly_rate)
    after_discount = apply_discount(before_discount, discount)
    trunc(Float.ceil(after_discount * 22))
  end

  def days_in_budget(budget, hourly_rate, discount) do
    discounted_daily_rate = apply_discount(daily_rate(hourly_rate), discount)
    Float.floor(budget / discounted_daily_rate, 1)    
  end
end
