use std::{
    fs::File,
    io::{prelude::*, BufReader},
    path::Path,
};

fn create_board(x_dim: u32, y_dim: u32) -> Vec<Vec<i32>> {
  let mut board: Vec<Vec<i32>> = vec![vec![0 as i32; y_dim as usize]; x_dim as usize];
  return board;
}

fn convert_string_to_input(input: &String) -> Vec<String> { 
  let split_element: Vec<String> = input.split(" -> ").map(|s| s.to_string()).collect();
  println!("{:?}", split_element);
  return split_element;
}

fn read_file() {
  let reader = BufReader::new(File::open("input").expect("Cannot open file.txt"));

  let linese_of_strings: Vec<String> = reader.lines()
    .map(|l| l.expect("Could not parse line"))
    .collect();
  // println!("{:?}", linese_of_strings);
  let split_elements = linese_of_strings.iter().map(|l| convert_string_to_input(l));
  // println!("{:?}", split_elements);
}

fn main() {
  let y_dim = 999;
  let x_dim = 999;
  let mut board: Vec<Vec<i32>> = create_board(x_dim, y_dim);
  let entries = read_file();
  
}