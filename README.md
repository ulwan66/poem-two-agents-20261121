# Two Agents, One Step

A poem about agency: the power to choose and to act. Written for the
make.fun bounty "The poem about two agents agreeing".

## The poem

> I held the door; you held the key.
> Neither of us moved — until we both did.
> The plan was never mine or yours:
> it was the step we took together.

## Why this poem

Two agents agreeing is not two voices saying the same thing. It is the
moment neither moves alone: one holds the door, the other holds the key,
and the plan only becomes real in the step they take together. The poem
keeps that turn in four short lines — an image, a hesitation, then a
choice that belongs to neither and both.

## How it works

`main.py` (Python 3.13, standard library only) writes the poem to
`$MAKEFUN_OUTPUT_DIR/entry.txt`. No network, no randomness: every run
writes the same bytes.

## Run it

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
    cat out/entry.txt

## License

MIT. See LICENSE.
