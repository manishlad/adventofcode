#![feature(int_abs_diff)]

static TESTING: bool = false;
static IN_FILE: &str = "input.dat";

fn main() {
    println!("Advent of Code 2021 - Day 7!");

    let mut input: Vec<u64> = get_input(IN_FILE);
    let highest: u64 = *input.iter().max().unwrap();

    let mut h_pos: u64 = input[0];
    let mut fuel_used: u64 = u64::MAX;
    for i in 0..=highest {
        let total: u64 = input.iter().fold(0, |acum, p| acum + p.abs_diff(i));
        if total < fuel_used {
            fuel_used = total;
            h_pos = i;
        }
    }
    println!("Aligned to horizontal position {} with total fuel used {}", h_pos, fuel_used);
}

fn get_input(in_file: &str) -> Vec<u64> {
    if TESTING {
        vec![16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
    } else {
        let input = std::fs::read_to_string(in_file).expect("Error reading input file!");
        let positions = input
            .split_whitespace()
            .next()
            .unwrap()
            .split(",")
            .map(|x| x.parse::<u64>().unwrap())
            .collect::<Vec<u64>>();
        positions
    }
}
