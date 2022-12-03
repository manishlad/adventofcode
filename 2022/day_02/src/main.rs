use std::collections::HashMap;

static TESTING: bool = false;

fn main() {
    println!("Advent of Code 2022 - Day 02!");

    let rps_map2: HashMap<&str, i32> = HashMap::from([
        ("A X", 1+3),
        ("A Y", 2+6),
        ("A Z", 3+0),
        ("B X", 1+0),
        ("B Y", 2+3),
        ("B Z", 3+6),
        ("C X", 1+6),
        ("C Y", 2+0),
        ("C Z", 3+3),
    ]);

    let given_strategy: String = get_input();
    let given_strategy_score: i32 = given_strategy.lines().fold(0, |acc, round| acc + rps_map2.get(round).unwrap());
    println!("Total score with given strategy is: {}", given_strategy_score);
}

fn get_input() -> String {
    let infile: String;
    if TESTING {
        infile = String::from("test_input.dat");
    } else {
        infile = String::from("puzzle_input.dat");
    }
    let input = std::fs::read_to_string(infile).expect("Error reading input file!");
    input
}
