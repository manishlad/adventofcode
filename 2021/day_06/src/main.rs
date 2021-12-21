static TESTING: bool = false;
static IN_FILE: &str = "input.dat";
static DAYS: i32 = 80;

fn main() {
    println!("Advent of Code - Day 6!");

    let mut l_fish_timers: Vec<u8> = get_input(TESTING);
    // println!("{:?}", l_fish_timers);

    for _i in 0..DAYS{
        l_fish_timers = simulate_days(l_fish_timers);
        // println!("{:?}", l_fish_timers);
    }
    println!("After {} days, there are a total of {:?} lanternfish", DAYS, l_fish_timers.len());
}

fn simulate_days(t0_timers: Vec<u8>) -> Vec<u8> {
    let mut spawn: usize = 0;
    let mut t1_timers: Vec<u8> = t0_timers
        .iter()
        .map(|&t| if t == 0 { spawn += 1; 6 } else { t - 1 })
        .collect();
    t1_timers.append(&mut vec![8; spawn]);
    t1_timers
}

fn get_input(testing: bool) -> Vec<u8> {
    if testing {
        vec![3, 4, 3, 1, 2]
    } else {
        let input = std::fs::read_to_string(IN_FILE).expect("Error reading input file!");
        let l_fish_timers = input
            .split_whitespace()
            .next()
            .unwrap()
            .split(",")
            .map(|x| x.parse::<u8>().unwrap())
            .collect::<Vec<u8>>();
        l_fish_timers
    }
}
