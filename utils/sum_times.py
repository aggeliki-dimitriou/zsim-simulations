import sys

def extract_time(filename):
     f = open(filename, "r")
     l=f.readlines()
     if len(l)>=6:
        line = l[5]
        time_string = (line.split(':')[1]).split("#")[0]
        time = int(time_string[1:-1])
        return time
     else:
        return 0 

def compute_arch(cfg,nn):
    #cfg = sys.argv[1]
    #nn = sys.argv[2]
    layers = []

    if nn == "alex":
        layers = ["conv1_a", "conv1_b","conv2_a", "conv2_b","conv3_a", "conv3_b","conv4_a", "conv4_b","conv5_a", "conv5_b", "pool1_a", "pool1_b","pool2_a", "pool2_b","pool3_a", "pool3_b", "fc1", "fc2", "fc3"]
    elif nn == "zfnet":
        layers = ["conv1","conv2","conv3","conv4","conv5","pool1","pool2","pool3", "fc1","fc2","fc3"]
    elif nn == "vggnet":
        layers = ["conv1","conv2","conv3","conv4","conv5", "conv6","conv7","conv8","conv9","conv10","conv11","conv12","conv13", "pool1","pool2","pool3", "pool4","pool5", "fc1","fc2","fc3"]
    elif nn == "resnet":
        layers = ["conv1","pool1","conv2_0_a","conv2_0_b","conv2_0_c","conv2_br","conv2_0_res","conv2_1_a","conv2_1_b","conv2_1_c","conv2_1_res","conv2_2_a","conv2_2_b","conv2_2_c", "conv2_2_res","conv3_0_a","conv3_0_b","conv3_0_c","conv3_br","conv3_0_res","conv3_1_a","conv3_1_b","conv3_1_c","conv3_1_res","conv3_2_a","conv3_2_b","conv3_2_c","conv3_2_res","conv3_3_a", "conv3_3_b","conv3_3_c","conv3_3_res","conv4_0_a","conv4_0_b","conv4_0_c","conv4_br","conv4_0_res","conv4_1_a","conv4_1_b","conv4_1_c","conv4_1_res","conv4_2_a","conv4_2_b","conv4_2_c", "conv4_2_res","conv4_3_a","conv4_3_b","conv4_3_c","conv4_3_res","conv4_4_a","conv4_4_b","conv4_4_c","conv4_4_res","conv4_5_a","conv4_5_b","conv4_5_c","conv4_5_res","conv5_0_a","conv5_0_b", "conv5_0_c","conv5_br","conv5_0_res","conv5_1_a","conv5_1_b","conv5_1_c","conv5_1_res","conv5_2_a","conv5_2_b","conv5_2_c","conv5_2_res","pool5","fc"]
    elif nn == "vgg19net":
        layers = ["conv1","conv2","conv3","conv4","conv5", "conv6","conv7","conv8","conv9","conv10","conv11","conv12","conv13","conv14","conv15","conv16","pool1","pool2","pool3", "pool4","pool5", "fc1","fc2","fc3"]
    path = "/home/aggeliki/zsim-uploads/"+cfg+"/"
    
    times = []
    for i in layers:
        filename = path+i+"/zsim.out"
        time = extract_time(filename)
        times.append(time)

    sum_of_times = sum(times)
    return sum_of_times
    #print("Times per layer: ", times)
    #print("Total time:", sum_of_times)

def main():
    cfgs = [["l1_alex_2","l4_alex_2","t1_alex_3","t4_alex_4"], ["l1_zf","l4_zf","t1_zf","t4_zf"], ["l1_vgg","l4_vgg","t1_vgg","t4_vgg"], ["l1_res","l4_res","t1_res","t4_res"], ["l1_vgg19","l4_vgg19","t1_vgg19","t4_vgg19"]]
    res = {}
    res_norm = {}
    for i in range(len(cfgs)):
        if i==0:
            nn="alex"
        elif i==1:
            nn="zfnet"
        if i==2:
            nn="vggnet"
        if i==3:
            nn="resnet"
        if i==4:
            nn="vgg19net"
        cnt=0
        l1=1
        for cfg in cfgs[i]:
            time = compute_arch(cfg,nn)
            if cnt==0:
                l1=time
            res[cfg]=time
            res_norm[cfg]=time/l1
            cnt+=1
     
    print(res)
    print(res_norm)
    return res_norm

main()
