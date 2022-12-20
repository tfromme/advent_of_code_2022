use std::env;
use std::fs;

fn read_file(args: &[String]) -> String {
    let file_path = &args[1];
    let contents = fs::read_to_string(file_path).expect("Cannot Read From File");
    contents
}

fn main() {
    let args: Vec<String> = env::args().collect();
    let contents = read_file(&args);
    println!("Hello, {:?}", contents);
}
