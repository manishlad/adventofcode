fn main() {
    println!("Advent of Code - Day 3!\n");

    let test_input_dat = get_test_input();
    let transposed_test_input_dat = transpose(&test_input_dat);
    gamma_epsilon(&transposed_test_input_dat, "Test");

    let input_dat = get_input();
    let transposed_input_dat = transpose(&input_dat);
    gamma_epsilon(&transposed_input_dat, "Actual");
}

fn gamma_epsilon(diagnostics: &Vec<Vec<u8>>, label: &str) {
    let (_gamma, _epsilon) = bit_counts(&diagnostics);

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
    let mut gamma: Vec<u8> = Vec::new();
    let mut epsilon: Vec<u8> = Vec::new();
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
            gamma.push(0);
            epsilon.push(1);
        } else {
            gamma.push(1);
            epsilon.push(0);
        }
    }
    (gamma, epsilon)
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
