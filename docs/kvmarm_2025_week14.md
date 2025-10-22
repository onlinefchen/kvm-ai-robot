# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-22 08:49:59

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 145
- **总 Thread 数**: 17

### 分类分布

- **PATCH**: 14 threads (116 邮件)
- **RFC**: 1 threads (12 邮件)
- **Other**: 2 threads (17 邮件)

---

## 📌 PATCH

共 14 个 thread

---

### Thread 1: [PATCH 0/3] Two minor fixups around FEAT_E2H0

**📧 邮件数**: 16 | **👥 参与者**: 3 | **📅 开始时间**: Sat, 29 Mar 2025 11:44:06 +0800

#### 🤖 AI 总结

本邮件线程讨论了与 FEAT_E2H0 相关的两个小修复补丁，主要集中在 ARM64 架构的 KVM（Kernel-based Virtual Machine）实现中。历史讨论中，Yicong Yang 提出了三个补丁，内容包括：更新缺失的特征寄存器、为 HCR_EL2.E2H RES1 添加 cpucap 以指示 FEAT_E2H0 不支持，以及修复在不支持 FEAT_E2H0 的平台上使用 kvm-arm.mode=nvhe 时的启动警告。

在之前的讨论中，Marc Zyngier 提出了对补丁的担忧，指出该补丁可能会在某些硬件上引发问题，并建议在热路径中避免使用相关功能。讨论还涉及到对 Apple 硬件的特殊处理需求。

本周的新讨论中，Yicong Yang 继续完善补丁，提出在特定情况下添加对 Apple 硬件的工作区，以避免在不支持 FEAT_E2H0 的平台上出现警告。Oliver Upton 提出了与 HPFAR_EL2 相关的多个补丁，旨在修复 KVM 中处理故障地址的逻辑，确保在处理异常时不重新遍历页表，从而避免潜在的系统崩溃。Marc Zyngier 对这些补丁进行了反馈，提出了一些改进建议。

总体来看，本周的讨论集中在确保 KVM 在不同硬件环境下的稳定性和兼容性上，特别是针对 ARM64 架构的细节调整。

#### 📝 邮件列表

1. **[03-29 11:44]** [PATCH 0/3] Two minor fixups around FEAT_E2H0
   - 发件人: Yicong Yang <yangyicong@huawei.com>
2. **[03-29 11:44]** [PATCH 2/3] arm64/cpufeature: Add cpucap for HCR_EL2.E2H RES1 (!FEAT_E2H0)
   - 发件人: Yicong Yang <yangyicong@huawei.com>
3. **[03-29 08:12]** Re: [PATCH 2/3] arm64/cpufeature: Add cpucap for HCR_EL2.E2H RES1 (!FEAT_E2H0)
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[03-29 16:41]** Re: [PATCH 2/3] arm64/cpufeature: Add cpucap for HCR_EL2.E2H RES1
 (!FEAT_E2H0)
   - 发件人: Yicong Yang <yangyicong@huawei.com>
5. **[03-29 10:41]** Re: [PATCH 2/3] arm64/cpufeature: Add cpucap for HCR_EL2.E2H RES1 (!FEAT_E2H0)
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[03-31 16:00]** Re: [PATCH 2/3] arm64/cpufeature: Add cpucap for HCR_EL2.E2H RES1
 (!FEAT_E2H0)
   - 发件人: Yicong Yang <yangyicong@huawei.com>
7. **[04-01 15:42]** [PATCH 0/3] KVM: arm64: Fixes for resolving the fault IPA
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[04-01 15:42]** [PATCH 1/3] KVM: arm64: Only read HPFAR_EL2 when value is architecturally valid
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[04-01 15:42]** [PATCH 2/3] arm64: Convert HPFAR_EL2 to sysreg table
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[04-01 15:42]** [PATCH 3/3] KVM: arm64: Don't translate FAR if invalid/unsafe
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[04-02 12:15]** Re: [PATCH 1/3] KVM: arm64: Only read HPFAR_EL2 when value is architecturally valid
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[04-02 12:30]** Re: [PATCH 1/3] KVM: arm64: Only read HPFAR_EL2 when value is architecturally valid
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[04-02 13:19]** Re: [PATCH 3/3] KVM: arm64: Don't translate FAR if invalid/unsafe
   - 发件人: Marc Zyngier <maz@kernel.org>
14. **[04-02 09:37]** Re: [PATCH 3/3] KVM: arm64: Don't translate FAR if invalid/unsafe
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
15. **[04-02 09:39]** Re: [PATCH 1/3] KVM: arm64: Only read HPFAR_EL2 when value is
 architecturally valid
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
16. **[04-02 18:01]** Re: [PATCH 3/3] KVM: arm64: Don't translate FAR if invalid/unsafe
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [PATCH 00/12] KVM: Make irqfd registration globally unique

**📧 邮件数**: 14 | **👥 参与者**: 2 | **📅 开始时间**: Tue,  1 Apr 2025 13:44:12 -0700

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（内核虚拟机）中 IRQFD（中断请求文件描述符）注册的改进，旨在确保 IRQFD 注册在全局范围内唯一。此次讨论包含了 12 个补丁（patch），主要由 Sean Christopherson 提出。

**原始问题**：
当前 KVM 允许将同一个 eventfd 绑定到多个 IRQFD，但这可能导致不一致的行为。补丁的目标是修改这一点，确保每个 eventfd 只能绑定到一个 IRQFD，从而避免潜在的用户空间错误。

**之前讨论要点**：
在历史讨论中，参与者们关注了 KVM 的 IRQFD 注册机制，指出现有实现可能导致用户空间的错误未被及时捕获，尤其是在进行虚拟机迁移时。补丁的提出旨在增强系统的健壮性，确保在多个虚拟机间不会出现 eventfd 的重复绑定。

**本周新讨论与进展**：
本周的讨论集中在补丁的具体实现上，包括：
1. **补丁 1-5**：重构 IRQFD 注册过程，确保在添加到事件等待队列时持有适当的锁，避免竞争条件。
2. **补丁 6**：引入新的等待队列助手，以支持完全独占的优先等待者。
3. **补丁 7**：禁止将多个 IRQFD 绑定到同一 eventfd，增强系统的错误处理能力。
4. **补丁 8-10**：调整现有的等待队列 API，简化代码并删除冗余的唯一性检查。
5. **补丁 11-12**：增加自测试，确保新机制的正确性和有效性。

总体来看，本周的讨论推动了补丁的逐步完善，确保 KVM 的 IRQFD 注册机制更加安全和高效。

#### 📝 邮件列表

1. **[04-01 13:44]** [PATCH 00/12] KVM: Make irqfd registration globally unique
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[04-01 13:44]** [PATCH 01/12] KVM: Use a local struct to do the initial vfs_poll() on
 an irqfd
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[04-01 13:44]** [PATCH 02/12] KVM: Acquire SCRU lock outside of irqfds.lock during assignment
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[04-01 13:44]** [PATCH 03/12] KVM: Initialize irqfd waitqueue callback when adding to
 the queue
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[04-01 13:44]** [PATCH 04/12] KVM: Add irqfd to KVM's list via the vfs_poll() callback
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[04-01 13:44]** [PATCH 05/12] KVM: Add irqfd to eventfd's waitqueue while holding irqfds.lock
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[04-01 13:44]** [PATCH 06/12] sched/wait: Add a waitqueue helper for fully exclusive
 priority waiters
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[04-01 13:44]** [PATCH 07/12] KVM: Disallow binding multiple irqfds to an eventfd
 with a priority waiter
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[04-01 13:44]** [PATCH 08/12] sched/wait: Drop WQ_FLAG_EXCLUSIVE from add_wait_queue_priority()
   - 发件人: Sean Christopherson <seanjc@google.com>
10. **[04-01 13:44]** [PATCH 09/12] KVM: Drop sanity check that per-VM list of irqfds is unique
   - 发件人: Sean Christopherson <seanjc@google.com>
11. **[04-01 13:44]** [PATCH 10/12] KVM: selftests: Assert that eventfd() succeeds in Xen
 shinfo test
   - 发件人: Sean Christopherson <seanjc@google.com>
12. **[04-01 13:44]** [PATCH 11/12] KVM: selftests: Add utilities to create eventfds and do KVM_IRQFD
   - 发件人: Sean Christopherson <seanjc@google.com>
13. **[04-01 13:44]** [PATCH 12/12] KVM: selftests: Add a KVM_IRQFD test to verify
 uniqueness requirements
   - 发件人: Sean Christopherson <seanjc@google.com>
14. **[04-03 00:10]** Re: [PATCH 06/12] sched/wait: Add a waitqueue helper for fully
 exclusive priority waiters
   - 发件人: K Prateek Nayak <kprateek.nayak@amd.com>

---

### Thread 3: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags

**📧 邮件数**: 13 | **👥 参与者**: 6 | **📅 开始时间**: Wed, 19 Mar 2025 14:04:29 -0300

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下允许使用 VMA（虚拟内存区域）标志进行可缓存的二级映射的补丁（PATCH v3 1/1）。该补丁旨在解决当前 QEMU 无法识别 VFIO（虚拟功能 I/O）创建的可缓存内存映射的问题。

在历史讨论中，参与者们探讨了如何在内存槽创建时进行有效的检查，以避免在运行的虚拟机中出现故障。Jason Gunthorpe 提出了在不支持 FWB（Faulting Write Back）硬件的情况下拒绝创建内存槽的建议，Catalin Marinas 和其他人对此表示支持，并讨论了如何通过侧信道与 KVM 进行通信以确保内存的可缓存性。

在本周的新讨论中，Jason Gunthorpe 强调了在内存槽创建期间进行保护性检查的重要性，以避免在没有 FWB 支持的情况下请求可缓存的 VFIO VMA。他认为，所有支持 CCA（Cache Coherency Architecture）的 ARM 系统都可能具备 FWB，因此继续沿用这一方向是合理的。此外，他指出必须阻止“回退到设备”的情况，以确保安全性，避免数据泄漏。

总体来看，讨论集中在如何确保 KVM 在处理可缓存内存映射时的安全性和有效性，以及对补丁的进一步完善建议。

#### 📝 邮件列表

1. **[03-19 14:04]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
2. **[03-19 18:11]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
3. **[03-19 16:22]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
4. **[03-19 21:48]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
5. **[03-26 08:31]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
6. **[03-26 07:53]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[03-26 15:42]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using VMA flags
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[03-26 09:10]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[03-26 18:02]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using VMA flags
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[03-26 11:24]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Sean Christopherson <seanjc@google.com>
11. **[03-26 11:51]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
12. **[03-31 11:44]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
13. **[03-31 11:56]** Re: [PATCH v3 1/1] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>

---

### Thread 4: [PATCH kvmtool v2 0/9] arm: Drop support for 32-bit kvmtool

**📧 邮件数**: 12 | **👥 参与者**: 1 | **📅 开始时间**: Fri,  4 Apr 2025 09:52:23 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM 工具的补丁系列，主要内容是移除对 32 位 ARM KVM 工具的支持。以下是讨论的主要内容：

1. **原始补丁内容**：补丁的主题是“[PATCH kvmtool v2 0/9] arm: Drop support for 32-bit kvmtool”，旨在彻底移除对 32 位 ARM KVM 工具的支持，因其在 Linux 5.7 版本中已被弃用。

2. **之前的讨论要点**：在历史讨论中，参与者提到 32 位 KVM 工具的使用几乎已经消亡，因此移除该支持是合理的。补丁的设计还包括将 ARM64 特有的功能移至主目录，合并相关的源文件，以简化代码结构。

3. **本周的新讨论与进展**：本周的讨论集中在补丁的具体实现上，包括将 ARM64 特有的头文件和源文件移至顶层目录，合并 kvm.c 和 kvm-cpu.c 文件，以及重命名目录以符合内核的命名规范。多个补丁已获得认可（Acked-by 和 Reviewed-by），并且在邮件中提到的具体修改包括删除多余的文件和更新 Makefile。

整体来看，讨论反映了对 KVM 工具代码结构的清理和优化，以适应当前的开发需求。

#### 📝 邮件列表

1. **[04-04 09:52]** [PATCH kvmtool v2 0/9] arm: Drop support for 32-bit kvmtool
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[04-04 09:52]** [PATCH kvmtool v2 1/9] Drop support for 32-bit arm
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[04-04 09:52]** [PATCH kvmtool v2 2/9] arm64: Move arm64-only features into main directory
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[04-04 09:52]** [PATCH kvmtool v2 3/9] arm64: Combine kvm.c
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[04-04 09:52]** [PATCH kvmtool v2 4/9] arm64: Merge kvm-cpu.c
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[04-04 09:52]** [PATCH kvmtool v2 5/9] arm64: Combine kvm-config-arch.h
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[04-04 09:52]** [PATCH kvmtool v2 6/9] arm64: Move remaining kvm/* headers
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[04-04 09:52]** [PATCH kvmtool v2 7/9] arm64: Move asm headers
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[04-04 09:52]** [PATCH kvmtool v2 8/9] arm64: Rename top-level directory
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[04-04 09:52]** [PATCH kvmtool v2 9/9] arm64: Get rid of the 'arm-common' include directory
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[04-04 09:52]** [PATCH v4 00/19] KVM: arm64: Debug cleanups
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
12. **[04-04 09:55]** Re: [PATCH v4 00/19] KVM: arm64: Debug cleanups
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 5: [PATCH v2 0/6] Add support for FEAT_{LS64, LS64_V} and related tests

**📧 邮件数**: 10 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 31 Mar 2025 17:43:14 +0800

#### 🤖 AI 总结

本邮件线程讨论了一个关于支持 Armv8.7 新特性的补丁集，主要是 FEAT_{LS64, LS64_V} 的实现及相关测试。该补丁集包含六个补丁，旨在为 Armv8.7 引入的单拷贝原子64字节加载和存储指令提供支持。

历史讨论中，补丁的主要内容是增加对 FEAT_{LS64, LS64_V} 的识别和启用，向用户空间暴露这些特性，并添加相关的硬件能力测试。同时，补丁还处理了在虚拟机中对不支持的内存访问的异常情况。

在本周的新讨论中，Yicong Yang 提出了补丁的具体实现，包括基础的 EL2 设置、对 FEAT_{LS64, LS64_V} 的支持、在 KVM 中启用这些特性，以及为其添加自测试。测试结果显示，补丁在主机和来宾环境中均能正确识别和处理这些特性。讨论中还涉及到一些细节问题，如如何处理数据中止异常和优化补丁的顺序。Oliver Upton 和 Suzuki K Poulose 对补丁提出了一些建议和修改意见，强调了代码的一致性和清晰性。

总体而言，本周的讨论集中在补丁的实现细节和测试结果上，推动了对新特性的支持进程。

#### 📝 邮件列表

1. **[03-31 17:43]** [PATCH v2 0/6] Add support for FEAT_{LS64, LS64_V} and related tests
   - 发件人: Yicong Yang <yangyicong@huawei.com>
2. **[03-31 17:43]** [PATCH v2 1/6] arm64: Provide basic EL2 setup for FEAT_{LS64, LS64_V} usage at EL0/1
   - 发件人: Yicong Yang <yangyicong@huawei.com>
3. **[03-31 17:43]** [PATCH v2 2/6] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Yicong Yang <yangyicong@huawei.com>
4. **[03-31 17:43]** [PATCH v2 3/6] KVM: arm64: Enable FEAT_{LS64, LS64_V} in the supported guest
   - 发件人: Yicong Yang <yangyicong@huawei.com>
5. **[03-31 17:43]** [PATCH v2 4/6] kselftest/arm64: Add HWCAP test for FEAT_{LS64, LS64_V}
   - 发件人: Yicong Yang <yangyicong@huawei.com>
6. **[03-31 17:43]** [PATCH v2 5/6] arm64: Add ESR.DFSC definition of unsupported exclusive or atomic access
   - 发件人: Yicong Yang <yangyicong@huawei.com>
7. **[03-31 17:43]** [PATCH v2 6/6] KVM: arm64: Handle DABT caused by LS64* instructions on unsupported memory
   - 发件人: Yicong Yang <yangyicong@huawei.com>
8. **[04-01 09:13]** Re: [PATCH v2 6/6] KVM: arm64: Handle DABT caused by LS64*
 instructions on unsupported memory
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[04-01 09:15]** Re: [PATCH v2 5/6] arm64: Add ESR.DFSC definition of unsupported
 exclusive or atomic access
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[04-03 10:04]** Re: [PATCH v2 1/6] arm64: Provide basic EL2 setup for FEAT_{LS64,
 LS64_V} usage at EL0/1
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>

---

### Thread 6: [PATCH v2 0/3] KVM: arm64: Fixes for resolving the fault IPA

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Wed,  2 Apr 2025 13:17:22 -0700

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理故障 IPA（Intermediate Physical Address）的问题，提出了一系列修复补丁。

**原始 patch/问题内容**：
本次讨论的补丁（PATCH v2 0/3）旨在解决 KVM 在确定故障 IPA 时的逻辑不一致性，特别是在处理 SEA（Synchronous External Abort）时，HPFAR_EL2 的值可能会被错误地读取，导致系统崩溃。

**之前讨论要点**：
在历史讨论中，参与者指出 KVM 的逻辑与架构规范不符，特别是在处理 HPFAR_EL2 时，缺乏对其有效性的检查。补丁的初版（v1）已针对这些问题进行了初步修改。

**本周的新讨论、进展或结论**：
本周的讨论集中在 Oliver Upton 提出的三个补丁上：
1. **补丁 1**：确保仅在 HPFAR_EL2 的值符合架构规范时读取该值。
2. **补丁 2**：将 HPFAR_EL2 转换为 sysreg 表，以便更好地管理寄存器字段。
3. **补丁 3**：在处理无效或不安全的 FAR 时，避免重新遍历页表，防止系统崩溃。

Marc Zyngier 对补丁表示认可，并给予了审核通过，最终 Oliver Upton 确认这些补丁已被应用到修复列表中。整体来看，本周的讨论推动了补丁的最终定稿和应用，解决了 KVM 在处理故障 IPA 时的关键问题。

#### 📝 邮件列表

1. **[04-02 13:17]** [PATCH v2 0/3] KVM: arm64: Fixes for resolving the fault IPA
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[04-02 13:17]** [PATCH v2 1/3] KVM: arm64: Only read HPFAR_EL2 when value is architecturally valid
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[04-02 13:17]** [PATCH v2 2/3] arm64: Convert HPFAR_EL2 to sysreg table
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[04-02 13:17]** [PATCH v2 3/3] KVM: arm64: Don't translate FAR if invalid/unsafe
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[04-02 22:48]** Re: [PATCH v2 1/3] KVM: arm64: Only read HPFAR_EL2 when value is architecturally valid
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[04-02 14:52]** Re: [PATCH v2 1/3] KVM: arm64: Only read HPFAR_EL2 when value is
 architecturally valid
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[04-02 22:53]** Re: [PATCH v2 0/3] KVM: arm64: Fixes for resolving the fault IPA
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[04-03 08:04]** Re: [PATCH v2 1/3] KVM: arm64: Only read HPFAR_EL2 when value is architecturally valid
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[04-03 08:45]** Re: [PATCH v2 0/3] KVM: arm64: Fixes for resolving the fault IPA
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 7: [PATCH v2 0/2] KVM : selftests: arm64: Explicitly set the page attrs
 to Inner-Shareable

**📧 邮件数**: 8 | **👥 参与者**: 4 | **📅 开始时间**: Sat,  5 Apr 2025 00:10:40 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）自测的两个补丁，主要集中在 ARM64 架构下的页面属性设置问题。

1. **原始补丁/问题内容**：
   - 本次补丁系列的目标是解决在某些实现（如 Neoverse-N3）中，由于内存属性冲突导致的 EL1 数据中止问题。具体来说，补丁将虚拟机创建时页面属性默认设置为 Inner-Shareable，以避免在执行原子指令时出现 IMPLEMENTATION DEFINED fault（FSC 0x35）。

2. **之前讨论要点**：
   - 之前的讨论中提到，KVM 自测库直接使用数字配置硬件字段，缺乏可读性和易出错性，因此需要引入宏定义来改善代码质量。此外，补丁还解决了原子指令在非共享属性下可能导致的数据中止问题，强调了 ARM 架构对共享属性的要求。

3. **本周的新讨论、进展或结论**：
   - 本周的讨论中，参与者对补丁的细节进行了深入探讨，特别是关于 Neoverse-N3 的实现行为和 ARM 文档中对原子指令的描述。最终，补丁经过讨论后被清理和优化，已被应用于修复，确保了 KVM 自测在 ARM64 环境下的稳定性和正确性。

#### 📝 邮件列表

1. **[04-05 00:10]** [PATCH v2 0/2] KVM : selftests: arm64: Explicitly set the page attrs
 to Inner-Shareable
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
2. **[04-05 00:10]** [PATCH v2 1/2] KVM: selftests: arm64: Introduce and use
 hardware-definition macros
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
3. **[04-05 00:10]** [PATCH v2 2/2] KVM: selftests: arm64: Explicitly set the page attrs
 to Inner-Shareable
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
4. **[04-04 17:31]** Re: [PATCH v2 2/2] KVM: selftests: arm64: Explicitly set the page
 attrs to Inner-Shareable
   - 发件人: Mingwei Zhang <mizhang@google.com>
5. **[04-04 19:50]** Re: [PATCH v2 2/2] KVM: selftests: arm64: Explicitly set the page
 attrs to Inner-Shareable
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[04-05 00:24]** Re: [PATCH v2 2/2] KVM: selftests: arm64: Explicitly set the page
 attrs to Inner-Shareable
   - 发件人: Mingwei Zhang <mizhang@google.com>
7. **[04-05 10:33]** Re: [PATCH v2 2/2] KVM: selftests: arm64: Explicitly set the page attrs to Inner-Shareable
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[04-06 11:16]** Re: [PATCH v2 0/2] KVM : selftests: arm64: Explicitly set the page attrs to Inner-Shareable
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 8: [PATCH v4 0/3] KVM: arm64: Separate the hyp FF-A buffers init from
 the host

**📧 邮件数**: 8 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 26 Mar 2025 11:38:58 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的补丁，主要涉及将 hypervisor FF-A（Firmware Framework for Arm）缓冲区的初始化与主机分离的问题。

**原始补丁内容**：
补丁的目标是将 hypervisor FF-A 缓冲区的初始化过程从主机 FF-A 映射调用路径中分离出来，以避免在受保护模式下，hypervisor 无法映射缓冲区时拒绝任何 FF-A 调用。此外，补丁还将 ffa_to_linux_err 的定义从 arm_ffa 驱动程序移动到 ffa 头文件中，以便 hyp 代码可以使用。

**之前讨论要点**：
在历史讨论中，参与者对补丁中“释放”调用的实现提出了疑问，特别是在 pKVM FF-A 代理模型下，hypervisor 的透明性问题引发了对 EL1（Exception Level 1）如何处理释放调用的讨论。Quentin Perret 认为 EL1 应该独立发出释放调用，而不依赖于 hypervisor 的行为。

**本周新讨论进展**：
本周的讨论中，Quentin Perret 表示希望补丁能够更好地实现 pKVM 的释放调用，而不是只做一半的工作。他对补丁的实现方式仍有疑虑，但愿意接受对规范的进一步解释。同时，Sudeep Holla 提到，在与 FF-A 规范的讨论中发现驱动程序的处理也存在问题，并计划将修复合并到 v6.15 版本中。这表明该补丁的实现仍需进一步完善和验证。

#### 📝 邮件列表

1. **[03-26 11:38]** [PATCH v4 0/3] KVM: arm64: Separate the hyp FF-A buffers init from
 the host
   - 发件人: Sebastian Ene <sebastianene@google.com>
2. **[03-26 11:39]** [PATCH v4 3/3] KVM: arm64: Release the ownership of the hyp rx buffer
 to Trustzone
   - 发件人: Sebastian Ene <sebastianene@google.com>
3. **[03-26 16:48]** Re: [PATCH v4 3/3] KVM: arm64: Release the ownership of the hyp rx
 buffer to Trustzone
   - 发件人: Quentin Perret <qperret@google.com>
4. **[03-27 09:37]** Re: [PATCH v4 3/3] KVM: arm64: Release the ownership of the hyp rx
 buffer to Trustzone
   - 发件人: Sebastian Ene <sebastianene@google.com>
5. **[03-28 11:39]** Re: [PATCH v4 3/3] KVM: arm64: Release the ownership of the hyp rx
 buffer to Trustzone
   - 发件人: Quentin Perret <qperret@google.com>
6. **[03-28 14:18]** Re: [PATCH v4 3/3] KVM: arm64: Release the ownership of the hyp rx
 buffer to Trustzone
   - 发件人: Sebastian Ene <sebastianene@google.com>
7. **[04-01 12:00]** Re: [PATCH v4 3/3] KVM: arm64: Release the ownership of the hyp rx
 buffer to Trustzone
   - 发件人: Quentin Perret <qperret@google.com>
8. **[04-01 13:55]** Re: [PATCH v4 3/3] KVM: arm64: Release the ownership of the hyp rx
 buffer to Trustzone
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>

---

### Thread 9: [PATCH v2 8/9] KVM: arm64: Stage-2 huge mappings for np-guests

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 3 Apr 2025 14:21:07 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下为非保护性虚拟机（np-guests）实现 Stage-2 大页映射的补丁（PATCH v2 8/9）。该补丁旨在优化内存管理，提高虚拟机的性能。

在之前的讨论中，参与者 Vincent Donnefort 提出了补丁的基本框架和实现思路，但并未详细记录历史讨论的内容。本周的新讨论中，Quentin Perret 对补丁的具体实现提出了一些建议和修改意见，包括对条件判断的调整、代码结构的优化以及对函数调用的简化等。他指出，某些代码逻辑可以合并，以减少不必要的循环，提高代码的可读性和效率。

本周的讨论进展表明，Quentin 将根据收到的反馈，准备发送一个新的版本（v3），以解决所有提出的问题和建议。这表明该补丁正在朝着更完善的方向发展，参与者们积极互动，推动补丁的改进。

#### 📝 邮件列表

1. **[04-03 14:21]** Re: [PATCH v2 8/9] KVM: arm64: Stage-2 huge mappings for np-guests
   - 发件人: Quentin Perret <qperret@google.com>
2. **[04-03 14:24]** Re: [PATCH v2 1/9] KVM: arm64: Handle huge mappings for np-guest CMOs
   - 发件人: Quentin Perret <qperret@google.com>
3. **[04-03 15:27]** Re: [PATCH v2 2/9] KVM: arm64: Add a range to
 __pkvm_host_share_guest()
   - 发件人: Quentin Perret <qperret@google.com>
4. **[04-03 15:31]** Re: [PATCH v2 3/9] KVM: arm64: Add a range to
 __pkvm_host_unshare_guest()
   - 发件人: Quentin Perret <qperret@google.com>
5. **[04-04 17:47]** Re: [PATCH v2 2/9] KVM: arm64: Add a range to
 __pkvm_host_share_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
6. **[04-04 18:05]** Re: [PATCH v2 3/9] KVM: arm64: Add a range to
 __pkvm_host_unshare_guest()
   - 发件人: Vincent Donnefort <vdonnefort@google.com>
7. **[04-04 18:08]** Re: [PATCH v2 8/9] KVM: arm64: Stage-2 huge mappings for np-guests
   - 发件人: Vincent Donnefort <vdonnefort@google.com>

---

### Thread 10: [PATCH 0/2] KVM : selftests: arm64: Explicitly set the page attrs to Inner-Shareable

**📧 邮件数**: 6 | **👥 参与者**: 2 | **📅 开始时间**: Fri,  4 Apr 2025 22:06:57 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 的自测试，特别是针对 arm64 架构的内存属性设置问题。

1. **原始 patch/问题的内容**：本次讨论的补丁系列主要解决了在某些实现（如 Neoverse-N3）中，内存属性冲突导致的 EL1 数据中止问题。补丁包括两个部分：第一部分是清理代码，使用适当的宏替代硬编码的数字；第二部分则是修复实际的错误，默认将虚拟机的页面属性设置为 Inner-Shareable。

2. **之前的讨论要点**：在之前的讨论中，参与者指出 KVM 自测试库中直接使用数字配置硬件字段的做法不够清晰，建议使用宏来提高可读性并减少错误风险。此外，关于内存属性不匹配导致的 EL1 数据中止问题，参与者讨论了相关的 ARM 文档条款，以便更好地理解问题的根源。

3. **本周的新讨论、进展或结论**：本周的讨论中，补丁的作者 Raghavendra Rao Ananta 提供了补丁的详细说明，并得到了其他参与者的反馈。Oliver Upton 指出，某些宏定义应放在更合适的文件中，并对补丁中的引用进行了更正。最终，双方达成一致，将引用的文档条款进行修正，以确保对问题的全面理解。

总体来看，本周的讨论集中在补丁的具体实现及其对内存属性设置的影响上，参与者们积极交流，确保补丁的准确性和有效性。

#### 📝 邮件列表

1. **[04-04 22:06]** [PATCH 0/2] KVM : selftests: arm64: Explicitly set the page attrs to Inner-Shareable
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
2. **[04-04 22:06]** [PATCH 1/2] KVM: selftests: arm64: Introduce and use
 hardware-definition macros
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
3. **[04-04 22:06]** [PATCH 2/2] KVM: selftests: arm64: Explicitly set the page attrs to Inner-Shareable
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
4. **[04-04 15:46]** Re: [PATCH 1/2] KVM: selftests: arm64: Introduce and use
 hardware-definition macros
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[04-04 16:01]** Re: [PATCH 2/2] KVM: selftests: arm64: Explicitly set the page attrs
 to Inner-Shareable
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[04-04 17:01]** Re: [PATCH 2/2] KVM: selftests: arm64: Explicitly set the page attrs
 to Inner-Shareable
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>

---

### Thread 11: [PATCH] smccc/kvm_guest: Remove the accidental semicolon

**📧 邮件数**: 5 | **👥 参与者**: 4 | **📅 开始时间**: Wed, 2 Apr 2025 14:44:01 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于一个补丁（patch），其内容为修复 `smccc/kvm_guest` 代码中的一个多余的分号。该补丁由 Shameer Kolothum 提交，目的是解决由内核测试机器人报告的警告，确保代码的正确性。

在历史讨论中，虽然没有具体的邮件记录，但可以推测之前有类似的补丁讨论过。Sudeep Holla 提到几天前有类似的补丁在讨论中，并询问这个补丁是否真的必要，因为它们也会被回溯到旧版本。

在本周的新讨论中，Shameer Kolothum 对 Sudeep 的提问表示歉意，并同意让 Sudeep 处理此补丁。Oliver Upton 则确认该补丁是针对本次发布周期内引入的错误，因此没有回溯的顾虑，并表示他会很快处理这个修复，因为他已经为 KVM 客户端驱动准备了一个类似的补丁。

总的来说，本周的讨论集中在确认补丁的必要性和处理方式上，最终达成一致，Oliver 将负责这个补丁的合并。

#### 📝 邮件列表

1. **[04-02 14:44]** [PATCH] smccc/kvm_guest: Remove the accidental semicolon
   - 发件人: Shameer Kolothum <shameerali.kolothum.thodi@huawei.com>
2. **[04-02 14:58]** Re: [PATCH] smccc/kvm_guest: Remove the accidental semicolon
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>
3. **[04-02 14:14]** RE: [PATCH] smccc/kvm_guest: Remove the accidental semicolon
   - 发件人: Shameerali Kolothum Thodi <shameerali.kolothum.thodi@huawei.com>
4. **[04-02 09:43]** Re: [PATCH] smccc/kvm_guest: Remove the accidental semicolon
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[04-03 10:01]** Re: [PATCH] smccc/kvm_guest: Remove the accidental semicolon
   - 发件人: Sudeep Holla <sudeep.holla@arm.com>

---

### Thread 12: [PATCH] smccc: kvm_guest: Align with DISCOVER_IMPL_CPUS ABI

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 27 Mar 2025 09:36:15 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个针对 Linux 内核的补丁，主题为“[PATCH] smccc: kvm_guest: Align with DISCOVER_IMPL_CPUS ABI”。该补丁的目的是修正超调用（hypercall）的 ABI，要求 R2 和 R3 参数必须为 0，因此在调用时显式传递 0。

在历史讨论中，Oliver Upton 提出了这个补丁，并指出它修复了之前的一个问题，即在实现 CPU 基础上启用错误修复的功能（Fixes: 86edf6bdcf05）。补丁涉及到的代码修改较小，仅在 `drivers/firmware/smccc/kvm_guest.c` 文件中进行了1处插入和1处删除。

在本周的新讨论中，Shameerali Kolothum 对该补丁进行了审核，并表示支持（Reviewed-by），确认补丁的有效性。随后，Oliver Upton 在另一封邮件中表示已将该补丁应用于修复列表，并感谢参与者的贡献。

总结来看，本周的讨论主要集中在补丁的审核和应用上，表明该补丁已获得认可并成功整合进代码库。

#### 📝 邮件列表

1. **[03-27 09:36]** [PATCH] smccc: kvm_guest: Align with DISCOVER_IMPL_CPUS ABI
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[03-31 06:54]** RE: [PATCH] smccc: kvm_guest: Align with DISCOVER_IMPL_CPUS ABI
   - 发件人: Shameerali Kolothum Thodi <shameerali.kolothum.thodi@huawei.com>
3. **[04-01 09:40]** Re: [PATCH] smccc: kvm_guest: Align with DISCOVER_IMPL_CPUS ABI
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 13: [PATCH v7 00/45] arm64: Support for Arm CCA in KVM

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 26 Mar 2025 02:14:35 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构在 KVM 中支持 Arm CCA 的补丁（PATCH v7 00/45）。历史讨论中，Emi Kisanuki 提到在使用基于 QEMU 的内部模拟器测试该补丁时，启动 Realm 时出现了系统崩溃，但他认为这并不是补丁本身的问题。Oliver Upton 也确认了这一点，指出崩溃是由于 RMM 需要提供一致的功能集，而不是内核错误，并提到 TF-RMM 最近通过隐藏 FEAT_MPAM 来解决了相关问题。

在本周的新讨论中，Emi Kisanuki 表达了感谢，并表示将会回溯应用 Oliver 提到的补丁。他验证了以下几点：1）在 ID 寄存器中禁用 MPAM 支持后，成功启动了 Realm 虚拟机；2）运行 kvm-unit-tests（使用 lkvm）时，除了 PMU 测试未通过（因为内部模拟器不支持 PMU），其他测试均已通过。这表明补丁在当前环境下的有效性和稳定性。

#### 📝 邮件列表

1. **[03-26 02:14]** RE: [PATCH v7 00/45] arm64: Support for Arm CCA in KVM
   - 发件人: Emi Kisanuki (Fujitsu) <fj0570is@fujitsu.com>
2. **[03-25 23:14]** Re: [PATCH v7 00/45] arm64: Support for Arm CCA in KVM
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[04-01 06:54]** RE: [PATCH v7 00/45] arm64: Support for Arm CCA in KVM
   - 发件人: Emi Kisanuki (Fujitsu) <fj0570is@fujitsu.com>

---

### Thread 14: [PATCH] arm64: Expose AIDR_EL1 via sysfs

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu,  3 Apr 2025 16:16:26 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个针对 ARM64 架构的补丁，主题为“通过 sysfs 暴露 AIDR_EL1”。该补丁旨在将 AIDR_EL1 寄存器的值暴露给虚拟机监控器（VMM），以便于虚拟机能够识别物理 CPU 实现。补丁的主要内容是将 AIDR_EL1 的值添加到 sysfs 中，与其他识别寄存器（如 MIDR_EL1 和 REVIDR_EL1）一起提供。

在历史讨论中，补丁的背景是 KVM PV ABI 最近新增了一项功能，允许虚拟机发现物理 CPU 的实现集合。虽然 MIDR_EL1 和 REVIDR_EL1 已经被暴露，但 AIDR_EL1 仍未提供，因此本补丁的提出是为了填补这一空白。

在本周的新讨论中，Oliver Upton 提出了补丁并详细说明了其目的和实现方式。Anshuman Khandual 对该补丁进行了审查，并表示认可，确认补丁的实现符合预期。整体来看，补丁得到了积极的反馈，预计将会被合并。

#### 📝 邮件列表

1. **[04-03 16:16]** [PATCH] arm64: Expose AIDR_EL1 via sysfs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[04-04 15:14]** Re: [PATCH] arm64: Expose AIDR_EL1 via sysfs
   - 发件人: Anshuman Khandual <anshuman.khandual@arm.com>

---

## 📌 RFC

共 1 个 thread

---

### Thread 1: [RFC PATCH 0/7] KVM: optee: Introduce OP-TEE Mediator for exposing secure world to KVM guests

**📧 邮件数**: 12 | **👥 参与者**: 2 | **📅 开始时间**: Tue,  1 Apr 2025 22:35:20 +0530

#### 🤖 AI 总结

本邮件线程讨论了一个名为“OP-TEE Mediator”的补丁系列，旨在为运行在arm64机器上的KVM（Kernel-based Virtual Machine）客户机提供与受信执行环境（TEE）如OP-TEE的交互能力。补丁的核心是创建一个TEE中介层，使得KVM客户机能够通过安全监控调用（SMC）与OP-TEE进行通信。

在历史讨论中，补丁的背景和设计被详细阐述。补丁提出了TEE中介的功能，允许客户机在不直接访问安全世界的情况下与OP-TEE进行交互。补丁还定义了在客户机创建和销毁时如何通知OP-TEE的机制。

本周的新讨论中，Yuvraj Sakshith提供了补丁的详细实现，包括多个补丁的具体内容，如增加对SMC的处理、创建和销毁虚拟机时的通知等。同时，Marc Zyngier对补丁提出了批评，认为将TEE的处理放在内核中并不合理，建议应由虚拟机监控程序（VMM）来处理与TEE的交互。他强调，KVM应保持与TEE的无关性，并允许TEE的实现完全在用户空间中进行。Yuvraj则回应了这些观点，解释了选择在内核中实现的原因，并表示愿意考虑改进设计。

总体来看，本周的讨论集中在补丁的实现细节及其设计合理性上，参与者对如何更有效地处理KVM与TEE之间的交互进行了深入探讨。

#### 📝 邮件列表

1. **[04-01 22:35]** [RFC PATCH 0/7] KVM: optee: Introduce OP-TEE Mediator for exposing secure world to KVM guests
   - 发件人: Yuvraj Sakshith <yuvraj.kernel@gmail.com>
2. **[04-01 22:35]** [RFC PATCH 1/7] firmware: smccc: Add macros for Trusted OS/App owner check on SMC value
   - 发件人: Yuvraj Sakshith <yuvraj.kernel@gmail.com>
3. **[04-01 22:35]** [RFC PATCH 2/7] tee: Add TEE Mediator module which aims to expose TEE to a KVM guest.
   - 发件人: Yuvraj Sakshith <yuvraj.kernel@gmail.com>
4. **[04-01 22:35]** [RFC PATCH 3/7] KVM: Notify TEE Mediator when KVM creates and destroys guests
   - 发件人: Yuvraj Sakshith <yuvraj.kernel@gmail.com>
5. **[04-01 22:35]** [RFC PATCH 4/7] KVM: arm64: Forward guest CPU state to TEE mediator on SMC trap
   - 发件人: Yuvraj Sakshith <yuvraj.kernel@gmail.com>
6. **[04-01 22:35]** [RFC PATCH 5/7] tee: optee: Add OPTEE_SMC_VM_CREATED and OPTEE_SMC_VM_DESTROYED
   - 发件人: Yuvraj Sakshith <yuvraj.kernel@gmail.com>
7. **[04-01 22:35]** [RFC PATCH 6/7] tee: optee: Add OP-TEE Mediator
   - 发件人: Yuvraj Sakshith <yuvraj.kernel@gmail.com>
8. **[04-01 22:35]** [RFC PATCH 7/7] tee: optee: Notify TEE Mediator on OP-TEE driver initialization and release
   - 发件人: Yuvraj Sakshith <yuvraj.kernel@gmail.com>
9. **[04-01 19:13]** Re: [RFC PATCH 0/7] KVM: optee: Introduce OP-TEE Mediator for exposing secure world to KVM guests
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[04-02 08:28]** Re: [RFC PATCH 0/7] KVM: optee: Introduce OP-TEE Mediator for
 exposing secure world to KVM guests
   - 发件人: Yuvraj Sakshith <yuvraj.kernel@gmail.com>
11. **[04-02 09:42]** Re: [RFC PATCH 0/7] KVM: optee: Introduce OP-TEE Mediator for exposing secure world to KVM guests
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[04-02 16:49]** Re: [RFC PATCH 0/7] KVM: optee: Introduce OP-TEE Mediator for
 exposing secure world to KVM guests
   - 发件人: Yuvraj Sakshith <yuvraj.kernel@gmail.com>

---

## 📌 Other

共 2 个 thread

---

### Thread 1: [6.1 PATCH RESEND 00/12] KVM: arm64: Backport of SVE fixes to v6.1

**📧 邮件数**: 13 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 04 Apr 2025 14:23:33 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（内核虚拟机）在 arm64 架构上 SVE（可扩展向量扩展）相关问题的补丁系列，主要集中在将 SVE 修复回移植到 v6.1 版本中。

**原始问题与补丁内容**：
本系列补丁的核心是将 Mark Rutland 提出的 SVE/KVM 交互修复回移植到 v6.1 版本。这些修复包括在进入 KVM 客户机时丢弃任何 SVE 状态、跟踪 FPSIMD 状态类型，以及明确 KVM 需要保存哪些浮点寄存器等。

**之前讨论要点**：
在历史讨论中，参与者讨论了 KVM 如何处理 SVE 状态，以及在不同情况下如何优化寄存器的保存与恢复。特别是，之前的实现依赖于 TIF_SVE 标志来管理寄存器的保存，这在性能上存在一定的局限性。

**本周新讨论与进展**：
本周的讨论集中在多个补丁的具体实现上，包括：
1. **不再使用 TIF_SVE**：补丁移除了 KVM 中对 TIF_SVE 的操作，简化了代码并优化了正常任务的处理。
2. **强制保存主机状态**：在加载 vCPU 时，确保主机的 FPSIMD/SVE 状态被保存并清除，以避免使用过时的数据。
3. **ZCR_EL{1,2} 的切换**：在客户机与主机之间的转换时，始终提前切换 ZCR_EL{1,2}，以确保主机能够正确处理 SVE 状态。

这些补丁的实施旨在提高 KVM 在处理 SVE 时的稳定性和性能，同时解决了历史上存在的一些问题。参与者们对补丁进行了审查，并表示支持其合并。

#### 📝 邮件列表

1. **[04-04 14:23]** [6.1 PATCH RESEND 00/12] KVM: arm64: Backport of SVE fixes to v6.1
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[04-04 14:23]** [PATCH RESEND 6.1 01/12] KVM: arm64: Discard any SVE state when
 entering KVM guests
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[04-04 14:23]** [PATCH RESEND 6.1 02/12] arm64/fpsimd: Track the saved FPSIMD
 state type separately to TIF_SVE
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[04-04 14:23]** [PATCH RESEND 6.1 03/12] arm64/fpsimd: Have KVM explicitly say
 which FP registers to save
   - 发件人: Mark Brown <broonie@kernel.org>
5. **[04-04 14:23]** [PATCH RESEND 6.1 04/12] arm64/fpsimd: Stop using TIF_SVE to
 manage register saving in KVM
   - 发件人: Mark Brown <broonie@kernel.org>
6. **[04-04 14:23]** [PATCH RESEND 6.1 05/12] KVM: arm64: Unconditionally save+flush
 host FPSIMD/SVE/SME state
   - 发件人: Mark Brown <broonie@kernel.org>
7. **[04-04 14:23]** [PATCH RESEND 6.1 06/12] KVM: arm64: Remove host FPSIMD saving for
 non-protected KVM
   - 发件人: Mark Brown <broonie@kernel.org>
8. **[04-04 14:23]** [PATCH RESEND 6.1 07/12] KVM: arm64: Remove VHE host restore of
 CPACR_EL1.ZEN
   - 发件人: Mark Brown <broonie@kernel.org>
9. **[04-04 14:23]** [PATCH RESEND 6.1 08/12] KVM: arm64: Remove VHE host restore of
 CPACR_EL1.SMEN
   - 发件人: Mark Brown <broonie@kernel.org>
10. **[04-04 14:23]** [PATCH RESEND 6.1 09/12] KVM: arm64: Refactor exit handlers
   - 发件人: Mark Brown <broonie@kernel.org>
11. **[04-04 14:23]** [PATCH RESEND 6.1 10/12] KVM: arm64: Mark some header functions as
 inline
   - 发件人: Mark Brown <broonie@kernel.org>
12. **[04-04 14:23]** [PATCH RESEND 6.1 11/12] KVM: arm64: Calculate cptr_el2 traps on
 activating traps
   - 发件人: Mark Brown <broonie@kernel.org>
13. **[04-04 14:23]** [PATCH RESEND 6.1 12/12] KVM: arm64: Eagerly switch ZCR_EL{1,2}
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 2: [kvm-unit-tests PATCH v3 0/5] arm64: Change the default QEMU CPU type to "max"

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Tue, 25 Mar 2025 16:00:28 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于对 KVM 单元测试的一个补丁（PATCH v3 0/5），其主要内容是将 arm64 的默认 QEMU CPU 类型更改为 "max"，以便测试最新的 Arm 特性。

在历史讨论中，Jean-Philippe Brucker 提出了这个补丁系列，重点是清理配置标志，并在配置过程中将 CPU 选择移动到 `./configure` 中，同时改进了帮助文本。补丁还引入了 `--qemu-cpu` 选项，允许用户设置运行的 CPU 类型，以便在 Arm 上默认启用所有 TCG 特性。Alexandru Elisei 对补丁表示支持，并建议在 RISC-V 上也使用 "max" 作为默认 CPU 类型。

在本周的新讨论中，Andrew Jones 对补丁进行了进一步的补充，提出需要在 `configure` 文件中添加对 RISC-V 的支持，使其在配置时也能将默认 CPU 设置为 "max"。这一修改旨在确保 RISC-V 和 arm64 一致性，提升整体功能性。

总结而言，当前讨论围绕着对 KVM 单元测试的补丁进行优化，主要集中在 CPU 类型的设置和兼容性上，进展顺利。

#### 📝 邮件列表

1. **[03-25 16:00]** [kvm-unit-tests PATCH v3 0/5] arm64: Change the default QEMU CPU type to "max"
   - 发件人: Jean-Philippe Brucker <jean-philippe@linaro.org>
2. **[03-25 16:00]** [kvm-unit-tests PATCH v3 4/5] configure: Add --qemu-cpu option
   - 发件人: Jean-Philippe Brucker <jean-philippe@linaro.org>
3. **[03-27 17:14]** Re: [kvm-unit-tests PATCH v3 4/5] configure: Add --qemu-cpu option
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
4. **[03-31 15:54]** Re: [kvm-unit-tests PATCH v3 4/5] configure: Add --qemu-cpu option
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

