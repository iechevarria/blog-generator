---
title: How to disable web search results in Windows 10 (as of 2021)
date: 2021-04-25
---

Windows 10 includes web/Bing search results in its local search. Not great! There used to be a simple toggle to turn off web results. As of April 2021, that simple toggle is gone. Really not great!

This method from [a recent reply](https://www.tenforums.com/tutorials/25016-turn-off-search-online-include-web-results-windows-10-a-10.html) to an old thread in a random Windows forum is the only way I was able to turn off web results.

### Steps to disable web results:

1. Open the Registry Editor (regedit)
1. Navigate to "Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Search"
1. Create a new "DWORD (32-bit) Value" and name it "BingSearchEnabled" by either right-clicking in the Registry Editor window or by clicking "Edit > New > ..."


![Creating a new DWORD](blog/how-to-disable-windows-10-web-search-results-2021/create-new-dword.png)

<ol start="4">
    <li>Make sure the value data for "BingSearchEnabled" is set to 0</li>
    <li>Either (1) restart the File Explorer process or (2) restart your computer</li>
    <li>Your Windows search bar should now be free of web/Bing search results</li>
</ol>


![No web results in the search bar now](blog/how-to-disable-windows-10-web-search-results-2021/no-web-results.png)
