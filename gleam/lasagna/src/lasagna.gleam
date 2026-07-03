pub fn expected_minutes_in_oven() {
  40
}

pub fn remaining_minutes_in_oven(actual_minutes_in_oven: Int) {
  expected_minutes_in_oven() - actual_minutes_in_oven
}

pub fn preparation_time_in_minutes(number_of_layers: Int) {
  number_of_layers * 2
}

pub fn total_time_in_minutes(number_of_layers: Int, actual_minutes_in_oven: Int) {
  preparation_time_in_minutes(number_of_layers) + actual_minutes_in_oven
}

pub fn alarm() {
  "Ding!"
}
