# Tables

## Question Flow

### 1384 - 1387

#### Overview

``` mermaid
---
title: Overview
---
graph TD
    A --> |q1-q4=No| F
    A --> |else| B
    B --> C
    C --> D
    D --> |q6=Yes| E
    D --> |q6=No| End
    E --> End
    F --> G
    G --> H
    H --> End
```

#### A. Employment Status
Employment status during the past week


``` mermaid
---
title: A
---
graph TD
    1 --> |Yes| 6
    1 --> |No| 2
    2 --> |Yes| 6
    2 --> |No| 3
    3 --> |Yes| 6
    3 --> |No| 4
    4 --> |Yes| 5
    4 --> |No| F
    5 --> 6
    6 --> B
```


#### B. Main Job

Characteristics of main job


``` mermaid
---
title: B
---
graph TD
    A --> 7
    7 --> 8
    8 --> 9
    9 --> 10
    10 --> 11
    11 --> 12
    12 --> 12.1
    12.1 --> 13[C]
```

#### C. Work Hours

Hours worked for all jobs

``` mermaid
---
title: C
---
graph TD
    B --> 13
    13 --> |< 44 h| 14
    13 --> |>= 44 h| 15
    14 --> 15
    15 --> |q13>q15| 16.1
    15 --> |q15>q13| 16.2
    15 --> |q15=q13| 17[D]
    16.1 --> 17
    16.2 --> 17
```

#### D. Increase Work

Willingness to increase hours worked and search for another job

```mermaid
---
title: D
---
graph TD
    17 --> |Yes| 18
    17 --> |No| 20
    18 --> |Yes| 19
    18 --> |No| 20
    19 --> 20
    20 --> |Yes| 21
    20 --> |No| 22
    21 --> 21.1
    21.1 --> 22
    22 --> |q6=No| End
    22 --> |q6=Yes| 23[E]
```

#### E. Second Job

Characteristics of second job

```mermaid
---
title: E
---
graph TD
    D --> |q6=Yes| 23
    23 --> 24
    24 --> 25
    25 --> End
```

#### F. Previous Work

Previous work experience

```mermaid
---
title: F
---
graph TD
    A --> |q1-q4=No| 26
    26 --> |Yes| 27
    26 --> |No| 32[G]
    27 --> 28
    28 --> 29
    29 --> 30
    30 --> 31
    31 --> 32
```

#### G. Job Search

Job search

```mermaid
---
title: G
---
graph TD
    F --> 32
    32 --> |Yes| 33
    32 --> |No| 35
    33 --> 34
    34 --> 38
    35 --> 36
    36 --> |Yes| 37
    36 --> |No| 41.1
    37 --> 38
    38 --> 38.1
    38.1 --> 39
    39 --> 40
    40 --> |Yes| 42[H]
    40 --> |No| 41
    41 --> 41.1 --> End
```

#### H. Desired Job

Characteristics of desired job

```mermaid
---
title: H
---
graph TD
    G --> 42
    42 --> 43
    43 --> End
```


### 1388 - 1401

#### Overview

``` mermaid
---
title: Overview
---
graph TD
    A --> |q1-q6=No| F
    A --> |else| B
    B --> C
    C --> D
    D --> |q8=Yes| E
    D --> |q8=No| End
    E --> End
    F --> G
    G --> H
    H --> End
```

#### A. Employment Status
Employment status during the past week


``` mermaid
---
title: A
---
graph TD
    1 --> |Yes| 8
    1 --> |No| 2
    2 --> |Yes| 8
    2 --> |No| 3
    3 --> |Yes| 8
    3 --> |No| 4
    4 --> |Yes| 8
    4 --> |No| 5
    5 --> |Yes| 8
    5 --> |No| 6
    6 --> |Yes| 7
    6 --> |No| 31[F]
    7 --> 8
    8 --> 9[B]
```


#### B. Main Job

Characteristics of main job


``` mermaid
---
title: B
---
graph TD
    A --> 9
    9 --> 10
    10 --> 11
    11 --> 12
    12 --> 13
    13 --> 14
    14 --> 15
    15 --> 16[C]
```

#### C. Work Hours

Hours worked for all jobs

``` mermaid
---
title: C
---
graph TD
    B --> 16
    16 --> |< 44 h| 17
    16 --> |>= 44 h| 18
    17 --> 18
    18 --> |q13>q15| 19
    18 --> |q15>q13| 20
    18 --> |q15=q13| 21[D]
    19 --> 21
    20 --> 21
```

#### D. Increase Work

Willingness to increase hours worked and search for another job

```mermaid
---
title: D
---
graph TD
    21 --> |Yes| 22
    21 --> |No| 24
    22 --> |Yes| 23
    22 --> |No| 24
    23 --> 24
    24 --> |Yes| 25
    24 --> |No| 27
    25 --> 26
    26 --> 27
    27 --> |q8=No| End
    27 --> |q8=Yes| 28[E]
```

#### E. Second Job

Characteristics of second job

```mermaid
---
title: E
---
graph TD
    D --> |q8=Yes| 28
    28 --> 29
    29 --> 30
    30 --> End
```

#### F&G. Job Search and Previous Work

Job search and Previous work experience


```mermaid
---
title: F & G
---
flowchart TB
    subgraph F
        direction TB
        A --> |q1-q6=No| 31
        31 --> |Yes| 32
        31 --> |No| 33
        32 --> |else| 34
        32 --> |no action| 33
        33 --> |1,2| 34
        34 --> |Yes| 35
        35 --> 36
        36 --> |1| 37
        36 --> |2-6| 39
        37 --> 38
        38 --> 39
    end

    39 --> |No| H

    subgraph G
        direction TB
        33 --> |3-7| 45
        33 --> |8-12| 47
        39 --> |Yes| 40
        40 --> 41
        41 --> 42
        42 --> 43
        43 --> 44
        45 --> |No| 46
        34 --> |No| 46
        45 --> |Yes| 47
        46 --> 47
    end
    44 --> H
    H --> End
    47 --> End
```


#### H. Desired Job

Characteristics of desired job

```mermaid
---
title: H
---
graph TD
    G --> 48
    48 --> 49
    49 --> 50
    50 --> End
```
