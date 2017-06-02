from lib import markup
from lib import graphs
import time
import re


class htmlExport():

    def __init__(self, users, hosts, vhosts, dnsres,
                 dnsrev, file, domain, shodan, tldres):
        self.users = users
        self.hosts = hosts
        self.vhost = vhosts
        self.fname = file
        self.dnsres = dnsres
        self.dnsrev = dnsrev
        self.domain = domain
        self.shodan = shodan
        self.tldres = tldres
        self.style = ""

    def styler(self):
        a = """
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <link rel="stylesheet" href="../lib/assets/css/bootstrap.min.css">
    <script src="../lib/assets/js/jquery-3.2.1.slim.min.js"></script>
    <script src="../lib/assets/js/tether.min.js"></script>
    <script src="../lib/assets/js/bootstrap.min.js"></script>
		"""
        self.style = a

    def writehtml(self):
        page = markup.page()
        page.html()
        self.styler()
        page.head(self.style)
        page.body()
        page.div(class_="container")

        page.div(class_="card")
        page.h1("Investigations Results", class_="card-header")
        page.div(class_="card-block")
        page.h3("Domain Scanned : " + self.domain,
                class_="card-title mb-2 text-muted")

        page.body("<br>")

        page.div(class_="card card-outline-success")
        page.h5("Dashboard", class_="card-header card-success card-inverse text-center")
        page.div(class_="card-block")
        graph = graphs.BarGraph('hBar')
        graph.values = [len(self.users), len(self.hosts), len(
            self.vhost), len(self.tldres), len(self.shodan)]
        graph.labels = ['Emails', 'hosts', 'Vhost', 'TLD', 'Shodan']
        graph.showValues = 1
        page.body(graph.create())
        page.div.close()
        page.div.close()

        page.body("<br>")
        page.div(class_="card  card-outline-success")
        page.h5("Emails", class_="card-header card-success card-inverse text-center")
        page.div(class_="card-block")
        if self.users != []:
            page.ul(class_="list-group")
            page.li(self.users, class_="list-group-item")
            page.ul.close()
        else:
            page.h6("No emails found")
        page.div.close()
        page.div.close()

        page.body("<br>")
        page.div(class_="card card-outline-success")
        page.h5("Hosts", class_="card-header card-success card-inverse text-center")
        page.div(class_="card-block")
        if self.hosts != []:
            page.ul(class_="list-group")
            page.li(self.hosts, class_="list-group-item")
            page.ul.close()
        else:
            page.h6("No hosts found")
        if self.vhost != []:
            page.ul(class_="list-group")
            page.li(self.vhost, class_="list-group-item")
            page.ul.close()
        page.div.close()
        page.div.close()

        page.div.close()
        page.div.close()
        page.div.close()
        page.body.close()
        page.html.close()

        file = open('outputs/' + self.domain + '_' + time.strftime("%d-%m-%Y_%H-%M-%S")+'_'+ self.fname+".html",'w')
        for x in page.content:
            try:
                file.write(x)
            except:
                print "Exception" + x  # send to logs
                pass
        file.close
        return "ok"
