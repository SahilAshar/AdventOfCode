use std::env;
use std::process;

use day1::Config;

fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::build(&args).unwrap_or_else(|err| {
        println!("Problem parsing arguments: {err}");
        process::exit(1);
    });

    println!("Searching for {}", config.query);
    println!("In file {}", config.query);

    if let Err(e) = day1::run(config) {
        println!("Application error: {e}");
        process::exit(1);
    }
}
