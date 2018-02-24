

infile = open("D-small-practice.in", "r")
outfile = open("output.txt", "w")

t = int( infile.readline() )

for run in xrange(t):
    line = infile.readline()
    parts = line.split(" ")
    k = int( parts[0] )
    c = int( parts[1] )
    s = int( parts[2] )

    outfile.write("Case #" + str(run+1) + ":")

    if( k == s ):
        for i in range(k):
            outfile.write( " " + str(i+1) )

    else:
        outfile.write(" IMPOSSIBLE")

    outfile.write("\n")

infile.close()
outfile.close()
