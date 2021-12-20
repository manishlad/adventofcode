use std::cmp::min;
use std::cmp::max;

fn main() {
    println!("Advent of Code - Day 5!");

    // let input: &str = "test_input.dat";
    // let mut ocean_floor: Vec<Vec<u16>> = vec![vec![0; 10]; 10];
    let input: &str = "input.dat";
    let mut ocean_floor: Vec<Vec<u16>> = vec![vec![0; 1000]; 1000];

    ocean_floor = read_input(input, ocean_floor);

    let overlaps: u16 = count_overlaps(ocean_floor);
    println!("Number of overlaps = {}", overlaps);
}

fn read_input(in_file: &str, mut ocean_floor: Vec<Vec<u16>>) -> Vec<Vec<u16>> {
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
            for y in min(start_xy[1], end_xy[1])..max(start_xy[1], end_xy[1])+1 {
                ocean_floor[y][start_xy[0]] += 1;
            }
        } else if start_xy[1] == end_xy[1] {
            for x in min(start_xy[0], end_xy[0])..max(start_xy[0], end_xy[0])+1 {
                ocean_floor[start_xy[1]][x] += 1;
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
