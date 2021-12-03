fn main() {
    println!("Advent of Code - Day 2!");

    let course = get_input();
    let cmd_list = get_cmd_list(course);

    let mut position = (0,0); // h_pos, depth
    navigate(&mut position, cmd_list);
    println!("Position = {:?}\nMultiplier = {}", position, position.0 * position.1);

    let course2 = get_input();
    let cmd_list2 = get_cmd_list(course2);
    let mut position2 = (0,0,0); // h_pos, depth, aim
    navigate2(&mut position2, cmd_list2);
    println!("Position = {:?}\nMultiplier = {}", position2, position2.0 * position2.1);

}

fn navigate(pos: &mut (i32, i32), cmd_list: Vec<(String, i32)>) {
    for cmd in cmd_list.iter() {
        match cmd.0.as_str() {
            "forward" => pos.0 += cmd.1,
            "down" => pos.1 += cmd.1,
            "up" => pos.1 -= cmd.1,
            &_ => print!("error"),
          }
    }
}

fn navigate2(pos: &mut (i32, i32, i32), cmd_list: Vec<(String, i32)>) {
    for cmd in cmd_list.iter() {
        match cmd.0.as_str() {
            "forward" => {pos.0 += cmd.1; pos.1 += pos.2 * cmd.1;},
            "down" => pos.2 += cmd.1,
            "up" => pos.2 -= cmd.1,
            &_ => print!("error"),
          }
    }
}

fn get_cmd_list(commands: Vec<String>) -> Vec<(String, i32)> {
    let mut cmd_list: Vec<(String, i32)> = Vec::new();
    for cmd in commands.iter() {
        let c: Vec<_> = cmd.split(' ').collect();
        cmd_list.push((String::from(c[0]), c[1].parse::<i32>().unwrap()));
    }
    cmd_list
}

fn get_test_input() -> Vec<String> {
    let input: Vec<String> = vec![
        "forward 5",
        "down 5",
        "forward 8",
        "up 3",
        "down 8",
        "forward 2"
        ].iter().map(|&s| s.into()).collect();
    input
}

fn get_input() -> Vec<String> {
    let commands = std::fs::read_to_string("input.dat").expect("Error reading input file!");
    let mut input_dat: Vec<String> = Vec::new();
    for command in commands.lines() {
        input_dat.push(String::from(command));
    }
    input_dat
}