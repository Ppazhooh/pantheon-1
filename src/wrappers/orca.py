#!/usr/bin/env python

from os import path
from subprocess import check_call

import arg_parser
import context
from helpers import utils


def main():
    args = arg_parser.sender_first()

    cc_repo = path.join(context.third_party_dir, 'Orca')
    rl_repo = path.join(context.third_party_dir, 'Orca', 'rl-module')
    send_src = path.join(cc_repo,'rl-module', 'orca-server-mahimahi')
    recv_src = path.join(cc_repo, 'rl-module', 'client')

    if args.option == 'deps':
        print 'libtbb-dev libasio-dev libalglib-dev libboost-system-dev'
        return

    if args.option == 'setup':
        utils.apply_patch('orca.patch', cc_repo)
        sh_cmd = './build.sh'
        check_call(sh_cmd, shell=True, cwd=cc_repo)
        return

    if args.option == 'receiver':
        cmd = [recv_src, args.ip , '1', args.port]
        # check_call(cmd, cwd=utils.tmp_dir)
        check_call(cmd)
        return




    if args.option == 'sender':
        report_period = '20'
        first_time = '4'
        scheme = 'cubic'
        actor_id = '0'
        downlink = 'down'
        uplink = 'up'
        delay_ms = '10'
        log_file = 'a'
        duration = '3000'
        qsize = '500'
        duration_steps = '0'

        cmd = [send_src, args.port,'/home/parsa/pantheon/third_party/Orca/rl-module', report_period , first_time, scheme , actor_id, 
        downlink, uplink, delay_ms, log_file, duration, qsize, duration_steps]
        # check_call(cmd, cwd=utils.tmp_dir)
        check_call(cmd)
        # sh_cmd = './orca-standalone-emulation.sh' + ' '+str(args.port)
        # check_call(sh_cmd, shell=True, cwd=cc_repo)
        return

if __name__ == '__main__':
    main()
