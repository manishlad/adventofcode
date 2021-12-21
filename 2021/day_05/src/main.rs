use std::cmp::max;
use std::cmp::min;
use std::iter::Iterator;

fn main() {
    println!("Advent of Code - Day 5!");

    // let input: &str = "test_input.dat";
    let input: &str = "input.dat";

    // let mut ocean_floor: Vec<Vec<u16>> = vec![vec![0; 10]; 10];
    let mut ocean_floor: Vec<Vec<u16>> = vec![vec![0; 1000]; 1000];
    ocean_floor = read_input(input, ocean_floor, false);
    let mut overlaps: u16 = count_overlaps(ocean_floor);
    println!("Part 1: Number of overlaps = {}", overlaps);

    // ocean_floor = vec![vec![0; 10]; 10];
    ocean_floor = vec![vec![0; 1000]; 1000];
    ocean_floor = read_input(input, ocean_floor, true);
    overlaps = count_overlaps(ocean_floor);
    println!(
        "Part 2: Number of overlaps including diagonals = {}",
        overlaps
    );
}

fn read_input(
    in_file: &str,
    mut ocean_floor: Vec<Vec<u16>>,
    include_diagonals: bool,
) -> Vec<Vec<u16>> {
    let input = std::fs::read_to_string(in_file).expect("Error reading input file!");

    for vertices in input.lines() {
        let row: Vec<&str> = vertices.split(" -> ").collect::<Vec<&str>>();

        let start_xy: Vec<usize> = row[0]
            .split(",")
            .map(|x| x.parse::<usize>().unwrap())
            .collect::<Vec<usize>>();
        let end_xy: Vec<usize> = row[1]
            .split(",")
            .map(|x| x.parse::<usize>().unwrap())
            .collect::<Vec<usize>>();

        if start_xy[0] == end_xy[0] {
            for y in min(start_xy[1], end_xy[1])..=max(start_xy[1], end_xy[1]) {
                ocean_floor[y][start_xy[0]] += 1;
            }
        } else if start_xy[1] == end_xy[1] {
            for x in min(start_xy[0], end_xy[0])..=max(start_xy[0], end_xy[0]) {
                ocean_floor[start_xy[1]][x] += 1;
            }
        } else if include_diagonals {
            let x_range: Box<dyn Iterator<Item = usize>>;
            let y_range: Box<dyn Iterator<Item = usize>>;
            if (start_xy[0] < end_xy[0]) && (start_xy[1] < end_xy[1]) {
                x_range = Box::new(start_xy[0]..=end_xy[0]) as Box<dyn Iterator<Item = usize>>;
                y_range = Box::new(start_xy[1]..=end_xy[1]) as Box<dyn Iterator<Item = usize>>;
            } else if (start_xy[0] < end_xy[0]) && (start_xy[1] > end_xy[1]) {
                x_range = Box::new(start_xy[0]..=end_xy[0]) as Box<dyn Iterator<Item = usize>>;
                y_range =
                    Box::new((end_xy[1]..=start_xy[1]).rev()) as Box<dyn Iterator<Item = usize>>;
            } else if (start_xy[0] > end_xy[0]) && (start_xy[1] < end_xy[1]) {
                x_range =
                    Box::new((end_xy[0]..=start_xy[0]).rev()) as Box<dyn Iterator<Item = usize>>;
                y_range = Box::new(start_xy[1]..=end_xy[1]) as Box<dyn Iterator<Item = usize>>;
            } else {
                // if (start_xy[0] > end_xy[0]) && (start_xy[1] > end_xy[1])
                x_range =
                    Box::new((end_xy[0]..=start_xy[0]).rev()) as Box<dyn Iterator<Item = usize>>;
                y_range =
                    Box::new((end_xy[1]..=start_xy[1]).rev()) as Box<dyn Iterator<Item = usize>>;
            }
            let coords = x_range.zip(y_range);
            for c in coords {
                ocean_floor[c.1][c.0] += 1;
            }
        }
    }
    ocean_floor
}

fn count_overlaps(ocean_floor: Vec<Vec<u16>>) -> u16 {
    let overlaps: u16 = ocean_floor.iter().fold(0, |acum, row| {
        acum + row
            .iter()
            .fold(0, |acum, position| acum + if position > &1 { 1 } else { 0 })
    });
    overlaps
}
