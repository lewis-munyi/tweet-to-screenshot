const fs = require('fs')
const neatCsv = require('neat-csv');
const puppeteer = require('puppeteer');
import {state, search_terms} from 'search';



(async () => {

    fs.readFile('./tweets.csv', async (err, data) => {
        if (err) {
            console.error(err)
            return
        }
        const tweet_csv = await neatCsv(data)

        for ([index, tweet] of tweet_csv.entries()) {
            for (term of search_terms) {
                if (tweet.tweet_text.includes(term)) {

                    const browser = await puppeteer.launch({ headless: state,
                        args: ['--no-sandbox', '--disable-setuid-sandbox']
                    });
                    const page = await browser.newPage();
                    // adjustments for this page (so we hit the desktop breakpoint)
                    page.setViewport({
                        width: 1000,
                        height: 600,
                        deviceScaleFactor: 2
                    });

                    await page.goto(tweet.tweet_link);

                    async function screenshotDOMElement(selector, padding = 0) {
                        const rect = await page.evaluate(selector => {
                            const element = document.querySelector(selector);
                            const {
                                x,
                                y,
                                width,
                                height
                            } = element.getBoundingClientRect();
                            return {
                                left: x,
                                top: y,
                                width,
                                height,
                                id: element.id
                            };
                        }, selector);

                        return await page.screenshot({
                            path: `images/image${index}.png`,
                            clip: {
                                x: rect.left - padding,
                                y: rect.top - padding,
                                width: rect.width + padding * 2,
                                height: rect.height + padding * 2
                            }
                        });
                    }

                    await screenshotDOMElement('div.tweet, div.permalink-tweet, div.js-actionable-user, div.js-actionable-tweet, div.js-original-tweet, div.with-social-proof, div.js-initial-focus, div.focus', 16);
                    await browser.close()
                }
            }
        }
    })

})();