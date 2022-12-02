static TESTING: bool = false;

fn main() {
    println!("Advent of Code 2022 - Day 01!");

    let calorie_groups = get_input();
    let mut total_calories_carried: Vec<i32> = Vec::new();
    for group in calorie_groups {
        total_calories_carried.push(total_calories(group));
    }
    total_calories_carried.sort();
    let part_1 = total_calories_carried.pop().unwrap();
    let part_2 =
        part_1 + total_calories_carried.pop().unwrap() + total_calories_carried.pop().unwrap();
    println!(
        "Part 1: The Elf carrying the most calories is carrying a total of {} calories",
        part_1
    );
    println!(
        "Part 2: The Three Elves carrying the most calories are carrying a total of {} calories",
        part_2
    );
}

fn total_calories(calories: Vec<i32>) -> i32 {
    let mut total: i32 = 0;
    for c in calories {
        total += c;
    }
    total
}

fn get_input() -> Vec<Vec<i32>> {
    let infile: String;
    if TESTING {
        infile = String::from("test_input.dat");
    } else {
        infile = String::from("puzzle_input.dat");
    }
    let input = std::fs::read_to_string(infile).expect("Error reading input file!");
    let calorie_groups = input.split("\n\n");
    let mut calories: Vec<Vec<i32>> = Vec::new();
    for group in calorie_groups {
        let mut individual_calories: Vec<i32> = Vec::new();
        for calorie in group.lines() {
            individual_calories.push(calorie.parse::<i32>().unwrap());
        }
        calories.push(individual_calories);
    }
    calories
}
