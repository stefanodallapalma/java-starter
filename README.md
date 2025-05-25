# Java Quality Tools Starter

A Java project template that demonstrates how to integrate quality tools from day one. This project showcases the integration of code formatting, static analysis, null safety checking, and automated code remediation tools into a cohesive development workflow.

## 🎯 Purpose

This starter project embodies the principle that **quality tools work best as part of the foundation rather than added later**. It demonstrates how integrating formatting standards, pre-commit hooks, static analysis, and code remediation from the beginning creates a better development culture where quality is woven into every line of code.

## 🛠️ Integrated Tools

### Code Formatting
- **Spotless** with **Palantir Java Format** - Ensures consistent code style across the entire codebase
- **Ratchet mode** - Only formats files changed since `origin/main` for efficient incremental formatting
- **Pre-commit integration** - Automatically formats staged Java files before commit

### Static Analysis & Null Safety
- **ErrorProne** - Catches common programming mistakes at compile time
- **NullAway** - Enforces null safety using JSpecify annotations
- **JSpecify** - Modern null safety annotations (`@Nullable`, `@NonNull`)

### Code Remediation
- **OpenRewrite** - Performs automated code transformations and applies best practices
- Custom recipes for:
    - Null annotation normalization (standardizes to JSpecify)
    - Static analysis improvements
    - JUnit to AssertJ migration
    - Logging framework migration to Log4j2
    - Code cleanup and unused code removal

### Development Workflow
- **Pre-commit hooks** - Automated formatting on commit
- **JaCoCo** - Code coverage reporting
- **JUnit 5** - Modern testing framework

## 📁 Project Structure

```
├── .pre-commit-config.yaml    # Pre-commit hook configuration
├── hooks/
│   └── spotless-apply.py      # Python script for pre-commit formatting
├── rewrite.yml                # OpenRewrite custom composite recipes
├── build.gradle               # Gradle build configuration with all tools
├── Makefile                   # Setup automation
└── src/
    ├── main/java/             # Source code
    └── test/java/             # Test code
```

## 🚀 Getting Started

### Prerequisites
- Java 17+
- Python 3.x (for pre-commit hooks)
- Git

### Setup
1. **Clone and initialize the project:**
   ```bash
   git clone https://github.com/stefanodallapalma/java-starter.git
   cd java-starter
   ```

2. **Set up pre-commit hooks:**
   ```bash
   make pre-commit-setup
   ```
   This will:
    - Install pre-commit
    - Configure Git hooks
    - Set up automatic formatting on commit

3. **Run initial build:**
   ```bash
   ./gradlew build
   ```

### Key Gradle Tasks
- `./gradlew spotlessCheck` - Check code formatting
- `./gradlew spotlessApply` - Apply code formatting
- `./gradlew rewriteRun` - Run OpenRewrite transformations
- `./gradlew rewriteDryRun` - Preview OpenRewrite changes
- `./gradlew build` - Full build with all checks

## 🧪 Try It Yourself

Create a file `src/main/java/org/example/DemoService.java` with the following intentionally problematic code:

```java
package org.example;
import java.util.*;
import java.util.List;

public class DemoService {
private String name;
    private List<String> items = new ArrayList<String>();

    public DemoService(String name) {
this.name = name;
    }

public String getName() { return name; }

    // This method can return null but isn't annotated
    public String findItem(String query) {
        for(String item : items) {
            if(item.equals(query)) return item;
        }
        return null;
    }

    // This method calls findItem but doesn't handle potential null
    public String processItem(String query) {
        String found = findItem(query);
        return found.toUpperCase(); // Potential NPE!
    }

    // Unused variable
    public void addItem(String item) {
        String temp = "processing";
        items.add(item);
    }
}
```

### What's Wrong With This Code?

1. **Formatting Issues:**
    - Inconsistent indentation
    - Missing spaces around operators
    - Redundant imports
    - Generic diamond operator not used

2. **NullAway/ErrorProne Issues:**
    - `findItem()` can return null but isn't annotated with `@Nullable`
    - `processItem()` calls `findItem()` without null checking
    - Unused variable in `addItem()`

3. **OpenRewrite Will Fix:**
    - Remove unused imports and variables
    - Replace double brace initialization
    - Use diamond operator for generics
    - Add proper null safety annotations
    - Apply static analysis improvements

### Testing the Tools

1. **Check formatting:**
   ```bash
   ./gradlew spotlessCheck
   ```
   This will fail due to formatting issues.

2. **Fix formatting:**
   ```bash
   ./gradlew spotlessApply
   ```
   This will automatically format the code.

3. **Try to compile (will fail due to NullAway):**
   ```bash
   ./gradlew compileJava
   ```
   ErrorProne/NullAway will catch the null safety violation.

4. **Fix with OpenRewrite:**
   ```bash
   ./gradlew rewriteRun
   ```
   This will add `@Nullable` annotations and fix some other issues.

5. **Verify everything works:**
   ```bash
   ./gradlew build
   ```

## 🔧 Configuration Details

### ErrorProne + NullAway
- Configured to treat null safety violations as compilation errors
- Uses JSpecify annotations (`org.jspecify.annotations.Nullable`)
- Only applies to main source code (tests are excluded)

### Spotless
- Uses Palantir Java Format for consistent styling
- Ratchet mode: only formats changed files
- Integrates with pre-commit hooks for automatic formatting

### OpenRewrite
- Custom recipes composition in `rewrite.yml`
- Normalizes all null annotations to JSpecify
- Applies comprehensive static analysis improvements
- Migrates JUnit assertions to AssertJ (for test files)

### Pre-commit Hooks
- Automatically runs `spotlessApply` when Java files are staged
- Re-stages formatted files to include changes in commit
- Python-based for cross-platform compatibility

## 🎯 Philosophy

This project is meant to show that integrating quality tools from day one:
- Creates better development habits
- Reduces technical debt accumulation
- Makes code reviews focus on logic rather than style
- Builds developer trust through consistent automation
- Makes quality improvements invisible and automatic

The goal isn't perfection, but **consistency** and **automation** that allows developers to focus on building features rather than fighting tooling.