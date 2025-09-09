package com.example.pl_connect.player;

import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class PlayerConfig {

    @Bean
    CommandLineRunner commandLineRunner(PlayerRepository repository) {
        return args -> {
            Player gabriel = new Player(
                    "Gabriel", "Brazil", "Goalkeeper",
                    25, 100, // ageYears, ageDays
                    300, 30, // mp, starts
                    2700.0, 0.0, 0.0, 0.0, // min, gls, ast, pk
                    0.0, 0.0, 0.0, 1.0, // crdy, crdr, xg, xag
                    "Arsenal" // team
            );

            Player alex = new Player(
                    "Alex", "England", "Defender",
                    28, 50, // ageYears, ageDays
                    320, 32, // mp, starts
                    2880.0, 2.0, 1.0, 0.0, // min, gls, ast, pk
                    0.0, 0.0, 0.0, 1.0, // crdy, crdr, xg, xag
                    "Liverpool" // team
            );

            repository.save(gabriel);
            repository.save(alex);
        };
    }
}
