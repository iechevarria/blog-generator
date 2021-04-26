---
title: How to disable web search results (as of 2021)
date: 2021-04-25
---

Windows 10 includes web/Bing search results in its local search. Not great! There used to be a simple toggle to turn off web/Bing results. As of April 2021, that simple toggle is gone. Really not great!

### Steps to disable 

- Open the Registry Editor (regedit)
- Navigate to "Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Search"
- Create a new "DWORD (32-bit) Value" and name it "BingSearchEnabled" by either right-clicking in the Registry Editor window or by clicking "Edit > New > ..."

![Creating a new DWORD](blog/how-to-disable-windows-10-web-search-results-april-2021/create-new-dword.png)

- Make sure the value data for "BingSearchEnabled" is set to 0
- Either (1) restart the file explorer process or (2) restart your computer
- Your Windows search bar should now be free of web/Bing search results

![No web results in the search bar now](blog/how-to-disable-windows-10-web-search-results-april-2021/no-web-results.png)

Source: [a recent reply](https://www.tenforums.com/tutorials/25016-turn-off-search-online-include-web-results-windows-10-a-10.html) in an old thread on a random forum
