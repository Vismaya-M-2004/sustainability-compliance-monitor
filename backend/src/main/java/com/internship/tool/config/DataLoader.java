package com.internship.tool.config;

import com.internship.tool.entity.User;
import com.internship.tool.repository.UserRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class DataLoader {

    @Bean
    CommandLineRunner loadData(UserRepository repository) {
        return args -> {

           // if (repository.count() == 0) {

                for (int i = 1; i <= 30; i++) {
                    User user = new User();
                    user.setName("User " + i);
                    user.setEmail("user" + i + "@test.com");

                    repository.save(user);
                }

                System.out.println("✅ 30 Users inserted!");
            
        };
    }
}