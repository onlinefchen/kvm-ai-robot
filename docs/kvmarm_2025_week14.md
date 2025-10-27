# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-27 09:53:44

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

本邮件讨论主题为针对 FEAT_E2H0 的两个小修复补丁。历史讨论中，Yicong Yang 提出了三个补丁，主要内容包括：添加缺失的特性寄存器更新、引入 cpucap 来识别 HCR_EL2.E2H RES1 的支持，以及修复在不支持 FEAT_E2H0 的平台上使用 kvm-arm.mode=nvhe 时的启动警告。Marc Zyngier 对补丁提出了疑问，指出可能会对某些硬件（如苹果设备）造成问题，并建议在热路径中避免使用相关功能。

在本周的新讨论中，Yicong Yang 表示将为苹果设备添加一个解决方案，并讨论了在早期 KVM 模式配置中检查 FEAT_E2H0 支持的必要性。Oliver Upton 提出了关于 KVM 中处理故障地址的补丁，指出现有逻辑与架构不符，建议在特定情况下避免重新遍历页表，以防止在异常情况下导致崩溃。Marc Zyngier 对 Oliver 的补丁提出了改进建议，双方就补丁的细节进行了深入讨论，最终达成共识，准备进一步修改补丁以提高代码的清晰度和安全性。整体来看，讨论集中在确保 KVM 在不同硬件平台上的兼容性和稳定性。

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

本邮件讨论的主题是关于 KVM（内核虚拟机）中 irqfd 注册的全局唯一性问题，主要由 Sean Christopherson 提出了一系列补丁（共12个），旨在增强 KVM 对事件文件描述符（eventfd）绑定的管理。

**原始问题与补丁内容**：
补丁的核心是确保一个 eventfd 在整个系统中只能绑定到一个 irqfd。当前 KVM 只禁止将 eventfd 绑定到同一虚拟机的多个 irqfds，但未能防止其绑定到多个虚拟机。此修改将改变 KVM 的 ABI，但预计不会对用户空间造成影响。

**之前讨论要点**：
在之前的讨论中，提到 KVM 需要增强对用户空间错误的防护，特别是在进行虚拟机迁移时，eventfd 可能会在多个虚拟机间转移，导致潜在的错误。

**本周新讨论与进展**：
本周的讨论集中在补丁的具体实现上，包括：
1. 引入了新的等待队列助手函数，以确保只有一个优先级等待者可以绑定到 eventfd。
2. 逐步重构了 irqfd 注册过程，确保在注册时持有必要的锁，避免竞争条件。
3. 增加了自测试，以验证 eventfd 和 irqfd 绑定的唯一性要求。
4. 其他补丁则对现有代码进行了清理和优化。

总的来说，本周的讨论推动了补丁的实施，确保 KVM 在处理事件文件描述符时的安全性和一致性。

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

在历史讨论中，参与者们探讨了如何在内存插槽创建时进行有效的检查，以避免在运行中的虚拟机中出现故障。Jason Gunthorpe 和 Catalin Marinas 提出，可能需要在没有 FWB（可写分配位）硬件的情况下拒绝创建内存插槽，并确保 KVM 能够支持可缓存的内存映射。

在本周的新讨论中，Jason Gunthorpe 强调了在内存插槽创建时进行保护性检查的重要性，建议如果 QEMU 请求一个没有 FWB 支持的可缓存 VFIO VMA 的内存插槽，则应立即失败以安全地中止迁移。此外，他指出，所有支持 CCA（缓存控制属性）的 ARM 系统可能都会具备 FWB，因此在使用 guest_memfd 时继续沿用这一方向是合理的。总体来看，参与者们一致认为需要加强对可缓存映射的安全性检查，以防止潜在的数据泄露问题。

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

本邮件讨论的主题是关于 KVM 工具的补丁，主要内容是移除对 32 位 KVM 工具的支持。以下是对讨论的总结：

1. **原始补丁内容**：补丁的目标是完全去除对 32 位 ARM KVM 工具的支持，因 Linux 内核在 5.7 版本中已停止支持 32 位 ARM KVM，且 64 位用户空间仍然可以支持 32 位客户机。

2. **历史讨论要点**：在之前的讨论中，参与者一致认为，考虑到 32 位 KVM 工具的使用几乎已不存在，移除相关支持是合适的。补丁的设计旨在简化代码结构，增强维护性。

3. **本周的新讨论与进展**：本周的邮件中，Oliver Upton 提出了多个补丁，逐步将 ARM 相关的代码和头文件整合到一个统一的结构中。补丁包括：
   - 将 ARM64 特有的功能移到主目录。
   - 合并 ARM 和 ARM64 的代码。
   - 移动剩余的 KVM 头文件到顶层 ARM 目录。
   - 最后将目录名称更改为与内核的命名方案一致。

这些补丁得到了 Marc Zyngier 和 Alexandru Elisei 的认可与审核，显示出社区对这一系列改动的支持。整体来看，此次讨论和补丁提交旨在清理和优化 KVM 工具的代码结构，提升其可维护性与一致性。

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

本邮件讨论的主题是关于为 Armv8.7 架构添加对 FEAT_{LS64, LS64_V} 的支持及相关测试的补丁集（PATCH v2 0/6）。该补丁集的主要内容包括：在 CPU 特性列表中添加识别和启用 FEAT_{LS64, LS64_V}，通过 HWCAP3 和 cpuinfo 向用户空间暴露这些特性的支持，添加相关的硬件能力测试，并处理虚拟机中对不支持的内存访问的异常。

历史讨论中，补丁集的背景是为了支持 Armv8.7 新引入的单副本原子 64 字节加载和存储指令，旨在提升用户空间驱动的性能，尤其是在实现直接工作队列条目（WQE）时。

本周的新讨论中，Yicong Yang 提交了补丁的多个部分，具体包括：
1. 提供基本的 EL2 设置以支持 FEAT_{LS64, LS64_V} 的使用。
2. 在 CPU 特性列表中添加 FEAT_{LS64, LS64_V} 的支持。
3. 在 KVM 中启用 FEAT_{LS64, LS64_V} 以支持相关特性。
4. 为 FEAT_{LS64, LS64_V} 添加自测。
5. 添加对不支持的独占或原子访问的 ESR.DFSC 定义。
6. 处理因 LS64* 指令在不支持的内存上操作而导致的数据异常（DABT）。

讨论中，Oliver Upton 提出了一些修改建议，包括补丁顺序调整和代码一致性问题。整体来看，补丁集的进展顺利，参与者积极反馈，推动了对新特性的支持。

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

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构中处理故障 IPA（Intermediate Physical Address）的修复补丁。此次讨论包含三个主要补丁，旨在解决 KVM 在确定故障 IPA 时的逻辑问题。

历史讨论中并未提供具体背景，但本周的讨论集中在 Oliver Upton 提出的三个补丁上。第一个补丁修正了 KVM 对 HPFAR_EL2（High Physical Fault Address Register）的读取逻辑，确保只有在值符合架构要求时才读取该寄存器。第二个补丁将 HPFAR_EL2 转换为系统寄存器表，以便后续使用更多寄存器字段。第三个补丁则避免在处理故障时重新遍历页表，以防止在 Hyp 模式下引发致命异常。

本周的讨论中，Marc Zyngier 对第一个补丁表示认可，并提出了一些细节上的建议。最终，Oliver Upton 在回应中确认了补丁的有效性，并表示已将其应用于修复中。这些补丁的实施将有助于提高 KVM 在 arm64 架构下的稳定性和可靠性。

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

本邮件线程讨论了针对 KVM 的 ARM64 自测试的两个补丁，主要目的是解决在某些实现（如 Neoverse-N3）中内存属性冲突导致的错误。

**原始补丁内容**：
补丁系列的核心是修复在 ARM64 KVM 自测试中，页面属性未明确设置为“内共享”（Inner-Shareable），这导致在执行原子指令时出现数据中止（data abort）错误（FSC 0x35）。补丁分为两个部分：
1. **补丁1**：引入硬件定义宏，替换直接使用的数字，以提高代码可读性并减少错误风险。
2. **补丁2**：修复实际问题，默认将自测试中创建的虚拟机的页面属性设置为“内共享”。

**之前讨论要点**：
在之前的讨论中，参与者对补丁的细节进行了审查，特别是关于 Neoverse-N3 的实现细节以及 ARM 架构对原子指令的保证。讨论中提到，KVM 自测试默认使用非共享属性，这导致原子指令在执行时可能不符合架构要求。

**本周新讨论与进展**：
本周的讨论集中在补丁的最终修订和清理上，参与者对补丁的引用和描述进行了调整，以确保准确性。最终，补丁被应用到修复列表中，确认了补丁的有效性和必要性。Raghavendra Rao Ananta 还根据讨论更新了补丁的变更日志，增加了与 LPA2 的交互说明。

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

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，主要涉及将 hypervisor FF-A（Firmware Framework for Arm）缓冲区的初始化与主机分离。

**原始补丁内容**：
补丁的核心是将 hypervisor 的 FF-A 缓冲区初始化过程从主机的 FF-A 映射调用路径中分离出来，以避免在受保护模式下，hypervisor 无法映射缓冲区时拒绝 FF-A 调用。此外，补丁还将错误映射的定义从 arm_ffa 驱动移动到 FF-A 头文件，以便 hyp 代码可以使用。

**之前讨论要点**：
在之前的讨论中，参与者对补丁中的“释放”调用提出了疑问，认为在 pKVM FF-A 代理模型中，hypervisor 应该是透明的，EL1（Exception Level 1）应直接发起释放调用，而不应依赖 hypervisor 的操作。讨论中还提到，当前实现可能导致缓冲区在未发出释放调用前就被覆盖，从而引发混淆。

**本周新讨论与进展**：
本周的讨论中，Quentin Perret 表达了对补丁实现的保留意见，认为应在 pKVM 中正确实现释放调用，而不是仅仅部分实现。Sudeep Holla 提到，之前的讨论中发现驱动程序在处理此问题时也存在错误，并已提交修复以在 v6.15 中合并。整体来看，讨论集中在如何确保补丁的正确性和一致性上。

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

本邮件线程讨论了一个关于 KVM（内核虚拟机）在 arm64 架构下为非保护性客户机（np-guests）实现 Stage-2 大页映射的补丁（PATCH v2 8/9）。该补丁旨在优化内存管理，提高虚拟化性能。

在历史讨论中，虽然没有具体的历史邮件，但可以推测之前的讨论集中在如何有效地处理大页映射及其对内存管理的影响上。

本周的新讨论中，参与者 Quentin Perret 和 Vincent Donnefort 对补丁进行了深入的技术审查。Quentin 提出了对补丁逻辑的修改建议，特别是在检查是否启用保护性 KVM 和处理大页映射的支持方面。他还建议对现有代码进行优化，以减少不必要的循环，提升代码效率。Vincent 赞同这些建议，并表示将对补丁进行相应的修改，准备提交一个新的版本（v3）以解决这些问题。

总体而言，本周的讨论集中在补丁的细节优化和代码清晰度上，参与者们积极互动，推动了补丁的改进进程。

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

本邮件讨论的主题是关于 KVM 的自测试，特别是针对 arm64 架构的内存属性设置问题。原始的 patch 包含两个部分，旨在解决在某些实现（如 Neoverse-N3）中，由于内存属性冲突导致的 EL1 数据中止（FSC 0x35）。

在之前的讨论中，参与者提到当前的 KVM 自测试库直接使用数字配置硬件字段，缺乏可读性且易出错，因此建议引入宏定义来替代这些数字，以提高代码的可维护性和清晰度。

本周的新讨论中，Raghavendra Rao Ananta 提出了两个补丁：第一个补丁（Patch-1）引入了硬件定义宏，替换了代码中的数字配置；第二个补丁（Patch-2）则明确将虚拟机的页面属性设置为 Inner-Shareable，以避免内存属性不匹配造成的数据中止。Oliver Upton 对补丁提出了建议，认为将宏定义放在 processor.h 中更为合适，并对文档引用进行了更正，以确保准确性。

总体来看，本周的讨论集中在如何通过代码改进来解决内存属性相关的问题，并提高 KVM 自测试的稳定性和可读性。

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

本邮件线程讨论的主题是一个针对 Linux 内核中 `smccc/kvm_guest` 的补丁，旨在移除代码中的一个多余分号。该补丁由 Shameer Kolothum 提交，修复了由内核测试机器人报告的警告，确保代码的整洁性和正确性。

在历史讨论中，虽然没有具体的邮件记录，但可以推测之前可能有类似的补丁讨论。Shameer 提到最近有类似的补丁出现在邮件列表中，且 KVM 的维护者已被抄送，表明该补丁的必要性和可能的回溯问题。

在本周的新讨论中，Sudeep Holla 提出是否有必要提交此补丁，考虑到之前的补丁可能已经被回溯。Oliver Upton 表示该补丁可以直接应用，因为相关的代码是在当前发布周期内引入的，并且他已经准备好将此修复合并到 KVM 客户端驱动中。最终，Shameer 同意将补丁提交给 Oliver，表明他对补丁的处理持开放态度。

总结来说，本周的讨论集中在补丁的必要性和合并流程上，最终达成一致，Oliver 将负责将该补丁合并。

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

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）中 SMCCC（Secure Monitor Call Convention）相关的补丁，主题为“[PATCH] smccc: kvm_guest: Align with DISCOVER_IMPL_CPUS ABI”。该补丁的目的是修正超调用的 ABI（应用二进制接口），要求 R2 和 R3 参数必须为 0，因此在调用时显式传递 0。

在历史讨论中，Oliver Upton 提出了这个补丁，并指出它修复了之前的一个问题，即在实现 CPU 时启用错误修正（Fixes: 86edf6bdcf05）。补丁的代码变更涉及到 `drivers/firmware/smccc/kvm_guest.c` 文件，进行了简单的增删操作。

在本周的新讨论中，Shameerali Kolothum 对补丁进行了审核并表示认可（Reviewed-by），确认了补丁的有效性。随后，Oliver Upton 在另一封邮件中宣布该补丁已被应用到修复列表中，并感谢参与者的贡献。

总结来看，此次讨论围绕着一个重要的补丁展开，经过审核后顺利应用，进一步完善了 KVM 的功能。

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

本邮件线程讨论了针对 ARM64 架构的 KVM 中对 Arm CCA（Cache Coherence Architecture）的支持，涉及到的补丁为「[PATCH v7 00/45] arm64: Support for Arm CCA in KVM」。

在历史讨论中，Emi Kisanuki 提到在使用基于 QEMU 的内部模拟器测试该补丁时，启动 Realm 时发生了 panic，但他认为这并不是补丁本身的问题。Oliver Upton 也确认这不是内核错误，而是 RMM（Realm Management Monitor）需要提供一致的功能集给 Realm，并提到 TF-RMM 最近通过隐藏 FEAT_MPAM 来解决了相关问题。

在本周的新讨论中，Emi Kisanuki 表示他们将回溯 Oliver 提到的补丁，并分享了测试结果：1）在禁用 ID 寄存器中的 MPAM 支持后，成功启动了 Realm 虚拟机；2）运行 kvm-unit-tests（使用 lkvm）时，除了 PMU 测试未通过外，其他测试均已通过（PMU 不被内部模拟器支持）。Emi 还附上了测试结果的确认信息。

总体来看，讨论围绕补丁的有效性和兼容性展开，参与者们对补丁的后续回溯和测试结果表示积极态度。

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

本邮件线程讨论了一个针对 ARM64 架构的补丁，主题为“通过 sysfs 暴露 AIDR_EL1”。该补丁的目的是在系统的 sysfs 中添加 AIDR_EL1 寄存器的暴露，以便虚拟机监控器（VMM）能够获取物理 CPU 实现的相关信息。补丁的具体内容包括在多个文件中添加 AIDR_EL1 的相关代码，使其与其他识别寄存器（如 MIDR_EL1 和 REVIDR_EL1）一起可用。

在历史讨论中，虽然没有具体的邮件记录，但补丁的背景是 KVM PV ABI 最近增加了一项功能，允许虚拟机发现物理 CPU 实现的集合。AIDR_EL1 的暴露是为了确保 VMM 能够获取必要的寄存器值，以便更好地调度虚拟机。

在本周的新讨论中，参与者 Oliver Upton 提出了补丁，并详细说明了其目的和实现方式。随后，另一位参与者 Anshuman Khandual 对该补丁进行了审查，并表示“看起来很好”（LGTM），确认了补丁的有效性并给予了支持。这表明该补丁得到了积极的反馈，可能会在后续的版本中被合并。

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

本邮件线程讨论了一个名为“OP-TEE Mediator”的补丁系列，旨在通过引入一个中介层，使得在arm64机器上运行的KVM客户机能够与安全世界中的OP-TEE进行交互。补丁的核心是实现一个TEE中介模块，允许客户机通过安全监控调用（SMC）与OP-TEE进行通信，而不被虚拟机监控器（hypervisor）阻止。

在历史讨论中，补丁的背景被阐述，指出KVM客户机无法直接与支持虚拟化的OP-TEE进行交互，因为客户机的SMC调用会被超出层（EL2）捕获。补丁系列的设计灵感来源于Xen的OP-TEE中介，提出了在内核中实现中介的理由，包括减少对用户空间库和虚拟机监控器的修改。

本周的新讨论中，Yuvraj Sakshith提出了多个补丁，涵盖了中介模块的初始化、客户机创建和销毁的通知、SMC调用的转发等功能。然而，Marc Zyngier对该设计提出了批评，认为将中介实现放在内核中并不合理，建议应将其放在虚拟机监控器中，以便更好地处理与TEE的交互。他强调，KVM应保持与TEE的无关性，并允许TEE在用户空间中实现，以提高灵活性和可维护性。

总体而言，讨论围绕如何有效地在KVM和OP-TEE之间建立通信机制展开，涉及设计选择的合理性和未来的可扩展性。

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

本邮件线程讨论了针对 KVM（内核虚拟机）在 arm64 架构下的 SVE（可扩展向量扩展）相关修复的补丁系列，主要是将这些修复回移植到 v6.1 版本。

**原始问题与补丁内容**：
最初的补丁系列由 Mark Brown 提交，主要针对 KVM 与 SVE 交互中的一些问题，包括在进入 KVM 客户机时清除 SVE 状态、跟踪 FPSIMD 状态类型、明确 KVM 要保存的 FP 寄存器等。这些补丁旨在提高 KVM 的稳定性和性能，特别是在处理 SVE 状态时。

**历史讨论要点**：
在之前的讨论中，开发者们关注了 KVM 如何处理 SVE 状态，特别是在系统调用和上下文切换时可能导致的状态丢失问题。补丁的设计考虑了性能优化和避免潜在的崩溃。

**本周新讨论与进展**：
本周的讨论集中在补丁的逐步提交上，涵盖了多个具体的实现细节，包括：
1. 移除 KVM 中对 TIF_SVE 的管理，以简化代码。
2. 确保在加载 vCPU 时无条件保存和刷新主机的 FPSIMD/SVE/SME 状态。
3. 在激活陷阱时计算 cptr_el2 的值，避免在每个 vCPU 结构中存储该值。
4. 通过在 guest 和 host 之间的转换中急切切换 ZCR_EL{1,2}，确保主机的 SVE 状态与客户机的最大 SVE VL 一致。

这些补丁的实施将有助于提高 KVM 的性能和可靠性，特别是在处理 SVE 状态时，减少了潜在的错误和复杂性。

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

本邮件线程讨论了一个关于 KVM 单元测试的补丁系列，主要目的是将 arm64 的默认 QEMU CPU 类型更改为 "max"，以便测试最新的 Arm 特性。

在历史讨论中，Jean-Philippe Brucker 提出了 v3 版本的补丁，清理了配置标志，并将 CPU 选择移至 `./configure` 文件中，改进了帮助文本。此外，补丁中引入了 `--qemu-cpu` 选项，允许用户设置运行的 CPU 类型，以便在 Arm 上默认启用所有 TCG 特性。Alexandru Elisei 对补丁表示支持，并建议如果将 RISC-V 的默认 CPU 类型也设置为 "max"，可以减少额外的修改。

在本周的新讨论中，Andrew Jones 对补丁进行了进一步的补充，建议在 `configure` 文件中将 arm64 和 RISC-V 的默认 CPU 类型都设置为 "max"。他提供了具体的代码修改建议，以确保 RISC-V 也能享受到相同的配置。

总体来看，讨论围绕着如何优化 KVM 单元测试的 CPU 配置展开，确保不同架构（如 arm64 和 RISC-V）能够利用最新的 CPU 特性。

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

