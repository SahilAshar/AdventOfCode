use std::error::Error;
use std::fs;

pub struct Config {
    pub file_path: String
}

impl Config {
    pub fn build(args: &Vec<String>) -> Result<Config, &'static str> {
        if args.len() < 2 {
            return Err("not enough arguments");
        }
        let file_path = args[1].clone();

        return Ok(Config { file_path });
    }
}

pub fn run(config: Config) -> Result<u64, Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)?;
    let split: Vec<&str> = contents.split("\n\n").collect();

    let mut elves: Vec<u64> = Vec::new();
    let mut elf_sum: u64 = 0;

    for elf in split.into_iter() {
        let cal = parse_each_elf(elf);
        elves.push(cal);
    }

    elves.sort();
    for cals in elves.drain((elves.len()- 3)..) {
        elf_sum += cals;
    }

    return Ok(elf_sum);
}

fn parse_each_elf(elf: &str) -> u64 {
    let mut elf_sum: u64 = 0;

    let split: Vec<&str> = elf.split("\n").collect();

    for str_num in split.into_iter() {
        if str_num.is_empty() {
            continue;
        }
        elf_sum += str_num.parse::<u64>().unwrap();
    }

    return elf_sum;
}