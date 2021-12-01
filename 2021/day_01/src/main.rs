use std::io;
use std::io::prelude::*;
use std::fs::File;

fn count_increases(depth_list: Vec<i32>){
    let mut counter = 0;
    let mut num_increased: i32 = 0;
    while counter < depth_list.len()-1 {
        if depth_list[counter] < depth_list[counter+1] {
            num_increased += 1;
        }
        counter += 1;
    }
    println!("Number of depth increases: {}", num_increased);    
}

fn count_three_measurement_increases(depth_list: Vec<i32>){
    let mut counter = 0;
    let mut num_increased: i32 = 0;
    let mut sums: Vec<i32> = Vec::new();
    while counter < depth_list.len()-2 {
        let sum = depth_list[counter] + depth_list[counter+1] + depth_list[counter+2];
        sums.push(sum);
        counter += 1;
    }
    counter = 0;
    while counter < sums.len()-1 {
        if sums[counter] < sums[counter+1] {
            num_increased += 1;
        }
        counter += 1;
    }
    println!("Number of three-measurement depth increases: {}", num_increased);    
}

fn main() {
    println!("Let's begin Advent of Code!");
    // let input_dat: Vec<i32> = Vec::from([199,
    //     200,
    //     208,
    //     210,
    //     200,
    //     207,
    //     240,
    //     269,
    //     260,
    //     263]);

    let mut file = File::open("input.dat").expect("Error reading file!");
    let mut contents = String::new();
    file.read_to_string(&mut contents).expect("Oops cannot reaf file");
    let mut input_dat: Vec<i32> = Vec::new();
    for s in contents.lines() {
        input_dat.push(s.parse::<i32>().unwrap());
    }

    // count_increases(input_dat);
    count_three_measurement_increases(input_dat);
}
