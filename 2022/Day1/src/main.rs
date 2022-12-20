use std::env;
use std::process;

use day1::Config;

fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::build(&args).unwrap_or_else(|err| {
        println!("Problem parsing arguments: {err}");
        process::exit(1);
    });

    println!("In file {}", config.file_path);

    let max_calorie_count = day1::run(config).unwrap_or_else(|err| {
        println!("Application error: {err}");
        process::exit(1);
    });

    println!("Max Calorie Count is: {}", max_calorie_count);
}
