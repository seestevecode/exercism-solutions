defmodule NameBadge do
  def print(id, name, department) do
    dept_or_owner = String.upcase(if department, do: department, else: "Owner")
    (if id, do: "[#{id}] - ", else: "") <> "#{name} - #{dept_or_owner}"
  end
end
