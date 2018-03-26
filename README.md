# bank-tech-test

A practice tech test from Makers Academy. I've chosen to do it with Python as
it fits in with my blog which can be found at:

## Getting Started

Fork this repo

## Running the tests

To install FreezeGun, simply:

```
pip install freezegun
```

To run tests you need to install Pytest in the root of the project.

```
pip install -U pytest
```

Then type pytest in terminal

## User stories

```
As an account holder,
I want to be able to deposit money into my account,
so that I can have somewhere to keep money.
```

```
As an account holder,
I want to be able to withdraw money from my account,
so that I can get my money back
```

```
As an account holder,
I want to be able to see any transactions I have made,
so that I can see how much money I have put in and withdrawn
```

```
As an account holder,
I want to be able to see when I have made transactions,
so that I can remind myself when I have made withdrawals and deposits
```

### Acceptance criteria

**Given** a client makes a deposit of 1000 on 10-01-2012  
**And** a deposit of 2000 on 13-01-2012  
**And** a withdrawal of 500 on 14-01-2012  
**When** she prints her bank statement  
**Then** she would see

```
date || credit || debit || balance
14/01/2012 || || 500.00 || 2500.00
13/01/2012 || 2000.00 || || 3000.00
10/01/2012 || 1000.00 || || 1000.00
```
