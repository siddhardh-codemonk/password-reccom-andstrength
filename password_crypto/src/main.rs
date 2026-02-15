use std::env;

fn encrypt(text: &str) -> String {
    text.chars()
        .map(|c| {
            if c.is_ascii_lowercase() {
                let x = c as u8 - b'a';
                let enc = (3 * x + 24) % 26;
                (enc + b'a') as char
            } else {
                c
            }
        })
        .collect()
}

fn decrypt(text: &str) -> String {
    text.chars()
        .map(|c| {
            if c.is_ascii_lowercase() {
                let x = c as u8 - b'a';
                let dec = (9 * (x + 26 - 24)) % 26;
                (dec + b'a') as char
            } else {
                c
            }
        })
        .collect()
}

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() < 3 {
        println!("Usage: cargo run [enc/dec] [text]");
        return;
    }

    let mode = &args[1];
    let input = &args[2];

    if mode == "enc" {
        println!("{}", encrypt(input));
    } else if mode == "dec" {
        println!("{}", decrypt(input));
    } else {
        println!("Invalid mode");
    }
}
