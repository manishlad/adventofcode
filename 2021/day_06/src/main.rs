use std::collections::HashMap;

static TESTING: bool = false;
static IN_FILE: &str = "input.dat";
static DAYS: usize = 256;

fn main() {
    println!("Advent of Code - Day 6!");

    let l_fish_timers: Vec<u8> = get_input(TESTING);


    //
    // 5th attempt
    //
    let mut sim_fish: HashMap<_, i64> = HashMap::new();

    for f in l_fish_timers {
        let count = sim_fish.entry(i64::from(f)).or_insert(0);
        *count += 1;
    }

    for _day in 0..DAYS {
        let spawning = *sim_fish.entry(0).or_insert(0);
        for timer in 0..=8 {
            let t1 = *sim_fish.entry(&timer+1).or_insert(0);
            sim_fish.insert(timer, t1);
        }
        let t6 = sim_fish.get_mut(&6).unwrap();
        *t6 += spawning;
        let t8 = sim_fish.get_mut(&8).unwrap();
        *t8 += spawning;
    }

    let total_fish = sim_fish.values().fold(0, |acc, f| acc + f);
    println!("After {} days, there are a total of {:?} lanternfish", DAYS, total_fish);


    // let mut sim_fish: Vec<(usize, u8)> = l_fish_timers
    //     .iter()
    //     .map(|&t| (DAYS, t))
    //     .collect::<Vec<(usize, u8)>>();
    // // println!("{:?}", sim_fish);

    //
    // 4th attempt
    // WORKING but still too slow
    //
    // let mut f = 0;
    // while f < sim_fish.len() {
    //     let mut days_remaining = sim_fish[f].0;
    //     let mut timer = sim_fish[f].1;
    //     let mut new_spawned: Vec<(usize, u8)> = Vec::new();
    //     if (timer == 8) && (days_remaining >= 2) {
    //         days_remaining -= 2;
    //         timer -= 2;
    //     }
    //     if (timer < 7) && (days_remaining >= (timer as usize)+1) {
    //         days_remaining -= timer as usize + 1;
    //         timer = 6;
    //         new_spawned.push((days_remaining, 8));
    //     }
    //     if (timer as usize) <= days_remaining {
    //         let spawns = days_remaining / ((timer as usize) + 1);
    //         for s in 1..=spawns {
    //             new_spawned.push((days_remaining - (s*7), 8))
    //         }
    //     }
    //     sim_fish.append(&mut new_spawned);
    //     f += 1;
    // }


    //
    // 3rd attempt
    // WORKING but slow
    //
    // let mut f = 0;
    // while f < sim_fish.len() {
    //     let mut days_remaining = sim_fish[f].0;
    //     let mut timer = sim_fish[f].1;
    //     let mut spawns: Vec<(usize, u8)> = Vec::new();
    //     if (timer < 7) && (days_remaining >= (timer as usize)+1) {
    //         days_remaining -= timer as usize + 1;
    //         timer = 6;
    //         spawns.push((days_remaining, 8));
    //     }
    //     while (timer as usize) < days_remaining {
    //         days_remaining -= timer as usize + 1;
    //         timer = 6;
    //         spawns.push((days_remaining, 8));
    //     }
    //     sim_fish.append(&mut spawns);
    //     f += 1;
    // }


    //
    // 2nd attempt
    // WORKING but slow
    //
    // let mut f = 0;
    // while f < sim_fish.len() {
    //     let mut days_remaining = sim_fish[f].0;
    //     let mut timer = sim_fish[f].1;
    //     while (days_remaining >= 0) && (i32::from(timer) < days_remaining) {
    //         days_remaining -= i32::from(timer)+1;
    //         timer = 6;
    //         sim_fish.push((days_remaining, 8));
    //     }
    //     f += 1;
    // }


    //
    // 1st attempt
    // Naive inefficient version
    //
    // for _i in 0..DAYS{
    //     l_fish_timers = simulate_day(l_fish_timers);
    // }

    // println!("After {} days, there are a total of {:?} lanternfish", DAYS, sim_fish.len());
}

//
// 1st attempt
// Naive inefficient version
//
// fn simulate_day(t0_timers: Vec<u8>) -> Vec<u8> {
//     let mut spawn: usize = 0;
//     let mut t1_timers: Vec<u8> = t0_timers
//         .iter()
//         .map(|&t| if t == 0 { spawn += 1; 6 } else { t - 1 })
//         .collect();
//     t1_timers.append(&mut vec![8; spawn]);
//     t1_timers
// }

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
