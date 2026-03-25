# Checking Logs
It's a good idea to check your logs for anything unusual when testing your mods.
You might also receive a bug report on your mod at some point with a log attached.

Logs for Void Crew are saved to the below directory, named `Player.log` and `Player-prev.log`. \
`C:\Users\[USER]\AppData\LocalLow\Hutlihut Games ApS\Void Crew`

If checking a multiplayer issue, don't forget to check logs of all players involved.

The most important things to look out for in a log are **Exceptions**. Exceptions mean that something in the code's process failed to execute.
When this happens, any remaining code will not have executed, which can escalate into larger problems.

Other important things to look out for are **Errors**. Errors mean that the game detected a problem, but still continued executing the code
to the best of its ability. This does not guarantee that things work as intended however.