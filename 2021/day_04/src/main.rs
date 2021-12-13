fn main() {
    println!("Advent of Code - Day 4!");

    let (draw_nums, mut boards) = get_input("input.dat");

    for n in draw_nums {
        let bingo: i32 = mark_boards(&mut boards, n);
        if bingo > 0 {
            println!("BINGO! Score {}", n * bingo);
            break;
        }
    }
}

fn mark_boards(boards: &mut Vec<Board>, n: i32) -> i32 {
    let mut bingo: i32 = 0;
    for b in boards {
        bingo = b.mark(n);
        if bingo > 0 {
            println!("BINGO! Board {:?}\n\nSum {}", b.numbers, bingo);
            break;
        }
    }
    bingo
}

fn get_input(in_file: &str) -> (Vec<i32>, Vec<Board>) {
    let input = std::fs::read_to_string(in_file).expect("Error reading input file!");
    let mut lines = input.lines();

    let draw_nums: Vec<i32> = lines
        .next()
        .unwrap()
        .split(",")
        .map(|n| n.parse::<i32>().unwrap())
        .collect::<Vec<i32>>();
    lines.next();

    let mut boards: Vec<Board> = Vec::new();
    let mut b: Board = create_board();
    for line in lines {
        let row: Vec<i32> = line
            .split_whitespace()
            .map(|n| n.parse::<i32>().unwrap())
            .collect::<Vec<i32>>();
        if row.is_empty() {
            boards.push(b);
            b = create_board();
            continue;
        }
        b.add_row(row);
    }
    (draw_nums, boards)
}

struct Board {
    numbers: Vec<Vec<i32>>,
    marks: [[bool; 5]; 5],
    transposed_marks: [[bool; 5]; 5],
}

fn create_board() -> Board {
    let b = Board {
        numbers: Vec::new(),
        marks: [[false; 5]; 5],
        transposed_marks: [[false; 5]; 5],
    };
    b
}

impl Board {
    pub fn add_row(&mut self, row: Vec<i32>) {
        self.numbers.push(row);
    }

    pub fn mark(&mut self, draw: i32) -> i32 {
        let element: (usize, usize) = match Board::find(&self, draw) {
            Ok(element) => element,
            Err(_) => return 0,
        };

        self.marks[element.0][element.1] = true;
        self.transposed_marks[element.1][element.0] = true;
        let bingo: i32 = self.check_marked();

        bingo
    }

    fn check_marked(&self) -> i32 {
        let mut sum: i32 = 0;
        for i in 0..self.numbers.len() {
            if self.marks[i]
                .into_iter()
                .fold(true, |acum, item| acum && item)
                ||
                self.transposed_marks[i]
                .into_iter()
                .fold(true, |acum, item| acum && item)
            {
                sum = self.unmarked_sum();
            }
        }
        sum
    }

    fn unmarked_sum(&self) -> i32 {
        let mut sum: i32 = 0;
        for i in 0..self.numbers.len() {
            for j in 0..self.numbers[i].len() {
                if self.marks[i][j] != true {
                    sum += self.numbers[i][j];
                }
            }
        }
        sum
    }

    fn find(&self, num: i32) -> Result<(usize, usize), &str> {
        let mut element = None;
        for i in 0..self.numbers.len() {
            for j in 0..self.numbers.len() {
                if self.numbers[i][j] == num {
                    element = Some((i.clone(), j.clone()));
                }
            }
        }
        match element {
            Some((_, _)) => Ok(element.unwrap()),
            None => Err("Not found"),
        }
    }
}
