




<h3 align="center">Search bot in telegram with DuckDuckGo API</h3>


  <ol>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Available Functions</a></li>
        <ul>
            <li><a href="#Start">Start</a></li>
            <li><a href="#Help">Help</a></li>
            <li><a href="#Search">Search</a></li>
            <li><a href="#Image">Image</a></li>
            <li><a href="#RandomImg">RandomImage</a></li>
        </ul>
  </ol>

## Getting Started

The Bot is invoked in telegram by searching the bot name and clicking the start button which sends a command
/start which invokes the bot's start command

### Prerequisites

* pip
  ```sh
  pip 
  ```

### Installation

1. Packages to be installed 
    <ul>
   <li>Telegram</li>
   <li>Telegram.ext</li>
   <li>Requests</li>
   <li>Re</li>
   <li>Json</li>
   <li>Time</li>
   </ul>




<!-- USAGE EXAMPLES -->
## Usage

Commands used to invoke functions :
<ol>
<li>Start -  <b>/start</b>
<ul><li>The <b>/start</b> command is used to invoke the start function in the search bot</li></ul></li>
<li>The <b>/help</b> command is used to display the list of command available in the bot and their explanations</li>
<li>Search - <b>/search</b><ul><li>The <b>/search</b> command is used to invoke the search function in the search bot which also searches for the word/sentence given as an argument.<br><br><b>For Example:</b> /search bike :- gives the result which are fetched from the Duck Duck Go Api service.</li></ul></li>
<li>Image - <b>/img</b><ul><li>The <b>/img</b> command is used to invoke the search function in the search bot which also searches images for the word/sentence given as an argument.<br><br><b>For Example:</b> /img bike :- gives the bike images which are fetched from the Duck Duck Go service.</li></ul></li>
<li>RandomImage - <b>/random</b><ul><li>The <b>/random</b> command is used to invoke the function in the search bot which fetches a random image from a API service and displays it in media group.<br><br><b>For Example:</b> /random :- gives the random image fetched from the picsum.photos Api service.</li></ul></li>
</ol>


