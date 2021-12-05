#![feature(drain_filter)]

fn main() {
    println!("Advent of Code - Day 3!\n");

    let test_input_dat = get_test_input();
    let transposed_test_input_dat = transpose(&test_input_dat);
    gamma_epsilon(&transposed_test_input_dat, "Test");
    o2gr_co2sr(&test_input_dat, &transposed_test_input_dat, "Test");

    let input_dat = get_input();
    let transposed_input_dat = transpose(&input_dat);
    gamma_epsilon(&transposed_input_dat, "Actual");
    o2gr_co2sr(&input_dat, &transposed_input_dat, "Actual");
}

fn o2gr_co2sr(diagnostics: &Vec<Vec<u8>>, transposed_diagnostics: &Vec<Vec<u8>>, label: &str) {
    let mut o2gr_diagnostics = diagnostics.clone();
    let mut co2sr_diagnostics = diagnostics.clone();
    let mut o2gr: usize = 0;
    let mut co2sr: usize = 0;

    // let (mut _o2gr, mut _co2sr) = bit_counts(&transposed_diagnostics);

    // for b in 0.._o2gr.len() {
    for b in 0..diagnostics[0].len() {
        let (mut _o2gr, mut _co2sr) = bit_counts(&transpose(&o2gr_diagnostics));

        if _o2gr[b] == 2 {
            // println!("Changing 2 to 1 {}, {:?}", _o2gr[b], _o2gr);
            _o2gr[b] = 1;
        }
        o2gr_diagnostics = o2gr_diagnostics
            .drain_filter(|x| x[b] == _o2gr[b])
            .collect::<Vec<_>>();
        if o2gr_diagnostics.len() == 1 {
            // println!("_o2gr {:?}\n", o2gr_diagnostics);
            o2gr = usize::from_str_radix(
                o2gr_diagnostics[0].clone()
                    .into_iter()
                    .map(|b| b.to_string())
                    .collect::<String>()
                    .as_str(),
                2,
            )
            .unwrap();
            // println!("o2gr = {}", o2gr);
            break;
        }
        // println!("_o2gr {:?}\n", o2gr_diagnostics);
    }

    for b in 0..diagnostics[0].len() {
        let (mut _o2gr, mut _co2sr) = bit_counts(&transpose(&co2sr_diagnostics));

        if _co2sr[b] == 2 {
            // println!("Changing 2 to 1 {}, {:?}", _co2sr[b], _co2sr);
            _co2sr[b] = 0;
            // println!("Changed 2 to 1 {}, {:?}", _co2sr[b], _co2sr);
        }
        co2sr_diagnostics = co2sr_diagnostics
            .drain_filter(|x| x[b] == _co2sr[b])
            .collect::<Vec<_>>();
        if co2sr_diagnostics.len() == 1 {
            // println!("_co2sr {:?}\n", co2sr_diagnostics);
            co2sr = usize::from_str_radix(
                co2sr_diagnostics[0].clone()
                    .into_iter()
                    .map(|b| b.to_string())
                    .collect::<String>()
                    .as_str(),
                2,
            )
            .unwrap();

            break;
        }
        // println!("_co2sr {:?}\n", co2sr_diagnostics);
    }

    let life_support_rating_consumption = o2gr * co2sr;

    // println!("\n\n");
    // println!("{:?}\n{:?}", o2gr_diagnostics, co2sr_diagnostics);
    println!(
        "Part 2 - {}:\n  oxygen generator rating = {}\n  CO2 scrubber rating = {}\n  life support rating consumption = {}\n\n",
        label, o2gr, co2sr, life_support_rating_consumption
    );
}

fn gamma_epsilon(diagnostics: &Vec<Vec<u8>>, label: &str) {
    let (_gamma, _epsilon) = bit_counts(&diagnostics);

    if _gamma.contains(&2) || _epsilon.contains(&2) {
        println!("ERROR: Could not get gamma epsilon values");
        return;
    }

    let gamma = usize::from_str_radix(
        _gamma
            .into_iter()
            .map(|b| b.to_string())
            .collect::<String>()
            .as_str(),
        2,
    )
    .unwrap();

    let epsilon = usize::from_str_radix(
        _epsilon
            .into_iter()
            .map(|b| b.to_string())
            .collect::<String>()
            .as_str(),
        2,
    )
    .unwrap();
    let power_consumption = gamma * epsilon;

    println!(
        "Part 1 - {}:\n  gamma   = {}\n  epsilon = {}\n  power consumption = {}\n\n",
        label, gamma, epsilon, power_consumption
    );
}

fn transpose(input_dat: &Vec<Vec<u8>>) -> Vec<Vec<u8>> {
    let length = input_dat[0].len();
    let mut transposed_dat: Vec<Vec<u8>> = Vec::new();
    for l in 0..length {
        let mut t: Vec<u8> = Vec::new();
        for i in 0..input_dat.len() {
            t.push(input_dat[i.clone()][l.clone()]);
        }
        transposed_dat.push(t);
    }
    transposed_dat
}

fn bit_counts(input: &Vec<Vec<u8>>) -> (Vec<u8>, Vec<u8>) {
    let mut most_commons: Vec<u8> = Vec::new();
    let mut least_commons: Vec<u8> = Vec::new();
    for i in 0..input.len() {
        let mut count_0: u16 = 0;
        let mut count_1: u16 = 0;
        for j in 0..input[i].len() {
            if input[i][j] == 0 {
                count_0 += 1;
            } else {
                count_1 += 1;
            }
        }
        if count_0 > count_1 {
            most_commons.push(0);
            least_commons.push(1);
        } else if count_0 < count_1 {
            most_commons.push(1);
            least_commons.push(0);
        } else {
            most_commons.push(2);
            least_commons.push(2);
        }
    }
    (most_commons, least_commons)
}

fn get_test_input() -> Vec<Vec<u8>> {
    let mut input_dat: Vec<Vec<u8>> = Vec::new();
    for test_diagnostics in TEST_INPUT.lines() {
        let digits: Vec<u8> = test_diagnostics
            .chars()
            .map(|d| d as u8 - 0x30)
            .collect::<Vec<u8>>();
        input_dat.push(digits);
    }
    input_dat
}

fn get_input() -> Vec<Vec<u8>> {
    let diagnostics = std::fs::read_to_string("input.dat").expect("Error reading input file!");
    let mut input_dat: Vec<Vec<u8>> = Vec::new();
    for line in diagnostics.lines() {
        let digits: Vec<u8> = line.chars().map(|d| d as u8 - 0x30).collect::<Vec<u8>>();
        input_dat.push(digits);
    }
    input_dat
}

const TEST_INPUT: &str = "00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010";
