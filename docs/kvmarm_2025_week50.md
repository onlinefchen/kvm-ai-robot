# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-12-15 00:25:41

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 222
- **总 Thread 数**: 20
- **大型 Thread** (>20封): 3 个

### 分类分布

- **PATCH**: 14 threads (206 邮件)
- **RFC**: 3 threads (7 邮件)
- **Bug Report**: 2 threads (5 邮件)
- **Other**: 1 threads (4 邮件)

---

## 📌 PATCH

共 14 个 thread

---

### Thread 1: [PATCH v5 00/24] ARM64 PMU Partitioning

**📧 邮件数**: 54 | **👥 参与者**: 4 | **📅 开始时间**: Tue,  9 Dec 2025 20:50:57 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的 PMU（性能监控单元）分区功能的实现，主要集中在 Colton Lewis 提出的补丁系列（PATCH v5 00/24）。该补丁旨在创建一种新的分区 PMU 方案，允许为虚拟机（VM）保留部分计数器，从而减少开销并提高性能。

**原始补丁/问题内容**：
补丁系列的核心是实现 PMU 的分区，使得虚拟机可以直接访问部分计数器，进而提高性能。补丁中包括了性能基准测试的详细信息，并在 KVM 论坛上进行了介绍。

**之前讨论要点**：
历史讨论中，参与者们关注了 PMU 分区的实现细节，包括如何在不同的上下文中管理 PMU 寄存器的访问，以及如何确保在分区模式下的性能和安全性。讨论中提到的关键点包括如何处理 PMU 中的事件过滤、上下文切换，以及如何在没有 FGT（细粒度陷阱）支持的情况下进行高效的寄存器访问。

**本周的新讨论、进展或结论**：
本周的讨论主要集中在补丁的具体实现和代码审查上。Colton 提出了多项补丁，涵盖了 PMU 寄存器的读写、事件过滤的强制执行、以及如何在分区模式下处理中断。Oliver Upton 提出了对补丁的建议，强调了代码的可读性和一致性，并提出了一些关于如何处理寄存器访问的改进意见。此外，还讨论了如何在 VM 层面上启用 PMU 分区的能力，并确保在创建 vCPU 之前进行适当的配置。整体来看，本周的讨论推动了 PMU 分区功能的进一步完善和代码质量的提升。

#### 📝 邮件列表

1. **[12-09 20:50]** [PATCH v5 00/24] ARM64 PMU Partitioning
   - 发件人: Colton Lewis <coltonlewis@google.com>
2. **[12-09 20:50]** [PATCH v5 01/24] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Colton Lewis <coltonlewis@google.com>
3. **[12-09 20:50]** [PATCH v5 02/24] KVM: arm64: Move arm_{psci,hypercalls}.h to an
 internal KVM path
   - 发件人: Colton Lewis <coltonlewis@google.com>
4. **[12-09 20:51]** [PATCH v5 03/24] KVM: arm64: Include KVM headers to get forward declarations
   - 发件人: Colton Lewis <coltonlewis@google.com>
5. **[12-09 20:51]** [PATCH v5 04/24] KVM: arm64: Move ARM specific headers in include/kvm
 to arch directory
   - 发件人: Colton Lewis <coltonlewis@google.com>
6. **[12-09 20:51]** [PATCH v5 05/24] KVM: arm64: Reorganize PMU includes
   - 发件人: Colton Lewis <coltonlewis@google.com>
7. **[12-09 20:51]** [PATCH v5 06/24] KVM: arm64: Reorganize PMU functions
   - 发件人: Colton Lewis <coltonlewis@google.com>
8. **[12-09 20:51]** [PATCH v5 07/24] perf: arm_pmuv3: Introduce method to partition the PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
9. **[12-09 20:51]** [PATCH v5 08/24] perf: arm_pmuv3: Generalize counter bitmasks
   - 发件人: Colton Lewis <coltonlewis@google.com>
10. **[12-09 20:51]** [PATCH v5 09/24] perf: arm_pmuv3: Keep out of guest counter partition
   - 发件人: Colton Lewis <coltonlewis@google.com>
11. **[12-09 20:51]** [PATCH v5 10/24] KVM: arm64: Set up FGT for Partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
12. **[12-09 20:51]** [PATCH v5 11/24] KVM: arm64: Writethrough trapped PMEVTYPER register
   - 发件人: Colton Lewis <coltonlewis@google.com>
13. **[12-09 20:51]** [PATCH v5 12/24] KVM: arm64: Use physical PMSELR for PMXEVTYPER if partitioned
   - 发件人: Colton Lewis <coltonlewis@google.com>
14. **[12-09 20:51]** [PATCH v5 13/24] KVM: arm64: Writethrough trapped PMOVS register
   - 发件人: Colton Lewis <coltonlewis@google.com>
15. **[12-09 20:51]** [PATCH v5 14/24] KVM: arm64: Write fast path PMU register handlers
   - 发件人: Colton Lewis <coltonlewis@google.com>
16. **[12-09 20:51]** [PATCH v5 15/24] KVM: arm64: Setup MDCR_EL2 to handle a partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
17. **[12-09 20:51]** [PATCH v5 16/24] KVM: arm64: Account for partitioning in PMCR_EL0 access
   - 发件人: Colton Lewis <coltonlewis@google.com>
18. **[12-09 20:51]** [PATCH v5 17/24] KVM: arm64: Context swap Partitioned PMU guest registers
   - 发件人: Colton Lewis <coltonlewis@google.com>
19. **[12-09 20:51]** [PATCH v5 18/24] KVM: arm64: Enforce PMU event filter at vcpu_load()
   - 发件人: Colton Lewis <coltonlewis@google.com>
20. **[12-09 20:51]** [PATCH v5 19/24] KVM: arm64: Implement lazy PMU context swaps
   - 发件人: Colton Lewis <coltonlewis@google.com>
21. **[12-09 20:51]** [PATCH v5 20/24] perf: arm_pmuv3: Handle IRQs for Partitioned PMU
 guest counters
   - 发件人: Colton Lewis <coltonlewis@google.com>
22. **[12-09 20:51]** [PATCH v5 21/24] KVM: arm64: Inject recorded guest interrupts
   - 发件人: Colton Lewis <coltonlewis@google.com>
23. **[12-09 20:51]** [PATCH v5 22/24] KVM: arm64: Add KVM_CAP to partition the PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
24. **[12-09 20:51]** [PATCH v5 23/24] KVM: selftests: Add find_bit to KVM library
   - 发件人: Colton Lewis <coltonlewis@google.com>
25. **[12-09 20:51]** [PATCH v5 24/24] KVM: arm64: selftests: Add test case for partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
26. **[12-09 13:08]** Re: [PATCH v5 10/24] KVM: arm64: Set up FGT for Partitioned PMU
   - 发件人: Oliver Upton <oupton@kernel.org>
27. **[12-09 13:14]** Re: [PATCH v5 12/24] KVM: arm64: Use physical PMSELR for PMXEVTYPER
 if partitioned
   - 发件人: Oliver Upton <oupton@kernel.org>
28. **[12-09 13:19]** Re: [PATCH v5 13/24] KVM: arm64: Writethrough trapped PMOVS register
   - 发件人: Oliver Upton <oupton@kernel.org>
29. **[12-09 13:33]** Re: [PATCH v5 15/24] KVM: arm64: Setup MDCR_EL2 to handle a
 partitioned PMU
   - 发件人: Oliver Upton <oupton@kernel.org>
30. **[12-09 13:37]** Re: [PATCH v5 16/24] KVM: arm64: Account for partitioning in
 PMCR_EL0 access
   - 发件人: Oliver Upton <oupton@kernel.org>
31. **[12-09 13:55]** Re: [PATCH v5 17/24] KVM: arm64: Context swap Partitioned PMU guest
 registers
   - 发件人: Oliver Upton <oupton@kernel.org>
32. **[12-09 14:00]** Re: [PATCH v5 18/24] KVM: arm64: Enforce PMU event filter at
 vcpu_load()
   - 发件人: Oliver Upton <oupton@kernel.org>
33. **[12-09 14:06]** Re: [PATCH v5 19/24] KVM: arm64: Implement lazy PMU context swaps
   - 发件人: Oliver Upton <oupton@kernel.org>
34. **[12-09 14:45]** Re: [PATCH v5 20/24] perf: arm_pmuv3: Handle IRQs for Partitioned
 PMU guest counters
   - 发件人: Oliver Upton <oupton@kernel.org>
35. **[12-09 14:52]** Re: [PATCH v5 21/24] KVM: arm64: Inject recorded guest interrupts
   - 发件人: Oliver Upton <oupton@kernel.org>
36. **[12-09 14:58]** Re: [PATCH v5 22/24] KVM: arm64: Add KVM_CAP to partition the PMU
   - 发件人: Oliver Upton <oupton@kernel.org>
37. **[12-09 15:00]** Re: [PATCH v5 00/24] ARM64 PMU Partitioning
   - 发件人: Oliver Upton <oupton@kernel.org>
38. **[12-10 10:54]** Re: [PATCH v5 01/24] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
39. **[12-11 02:31]** Re: [PATCH v5 11/24] KVM: arm64: Writethrough trapped PMEVTYPER
 register
   - 发件人: kernel test robot <lkp@intel.com>
40. **[12-11 04:21]** Re: [PATCH v5 09/24] perf: arm_pmuv3: Keep out of guest counter
 partition
   - 发件人: kernel test robot <lkp@intel.com>
41. **[12-12 19:22]** Re: [PATCH v5 01/24] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Colton Lewis <coltonlewis@google.com>
42. **[12-12 20:27]** Re: [PATCH v5 11/24] KVM: arm64: Writethrough trapped PMEVTYPER register
   - 发件人: Colton Lewis <coltonlewis@google.com>
43. **[12-12 20:29]** Re: [PATCH v5 09/24] perf: arm_pmuv3: Keep out of guest counter partition
   - 发件人: Colton Lewis <coltonlewis@google.com>
44. **[12-12 20:51]** Re: [PATCH v5 10/24] KVM: arm64: Set up FGT for Partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
45. **[12-12 20:54]** Re: [PATCH v5 12/24] KVM: arm64: Use physical PMSELR for PMXEVTYPER
 if partitioned
   - 发件人: Colton Lewis <coltonlewis@google.com>
46. **[12-12 21:06]** Re: [PATCH v5 13/24] KVM: arm64: Writethrough trapped PMOVS register
   - 发件人: Colton Lewis <coltonlewis@google.com>
47. **[12-12 21:22]** Re: [PATCH v5 15/24] KVM: arm64: Setup MDCR_EL2 to handle a
 partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
48. **[12-12 21:31]** Re: [PATCH v5 16/24] KVM: arm64: Account for partitioning in PMCR_EL0 access
   - 发件人: Colton Lewis <coltonlewis@google.com>
49. **[12-12 21:57]** Re: [PATCH v5 17/24] KVM: arm64: Context swap Partitioned PMU guest registers
   - 发件人: Colton Lewis <coltonlewis@google.com>
50. **[12-12 21:59]** Re: [PATCH v5 18/24] KVM: arm64: Enforce PMU event filter at vcpu_load()
   - 发件人: Colton Lewis <coltonlewis@google.com>
51. **[12-12 22:25]** Re: [PATCH v5 19/24] KVM: arm64: Implement lazy PMU context swaps
   - 发件人: Colton Lewis <coltonlewis@google.com>
52. **[12-12 22:36]** Re: [PATCH v5 20/24] perf: arm_pmuv3: Handle IRQs for Partitioned PMU
 guest counters
   - 发件人: Colton Lewis <coltonlewis@google.com>
53. **[12-12 22:55]** Re: [PATCH v5 21/24] KVM: arm64: Inject recorded guest interrupts
   - 发件人: Colton Lewis <coltonlewis@google.com>
54. **[12-12 22:59]** Re: [PATCH v5 22/24] KVM: arm64: Add KVM_CAP to partition the PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>

---

### Thread 2: [PATCH 00/32] KVM: arm64: Introduce vGIC-v5 with PPI support

**📧 邮件数**: 36 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 12 Dec 2025 15:22:34 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是引入对 KVM 中 GICv5 的支持，特别是针对 ARM64 架构的虚拟化。以下是讨论的主要内容总结：

1. **原始 Patch/问题内容**：
   本系列补丁（共 32 个）旨在为 KVM 的 ARM64 实现引入 GICv5（虚拟通用中断控制器 v5），并支持 PPI（私有中断）。初步实现仅涉及 PPI，后续补丁将添加对 SPI（共享中断）和 LPI（本地中断）的支持。

2. **之前讨论要点**：
   - 之前的讨论集中在 GICv5 的架构特性及其与现有 GICv3 的差异上。GICv5 采用了不同的中断 ID 编码方式，且不再使用 AP 列表来管理中断状态，而是通过 ICH_PPI_* 寄存器直接管理 PPIs 的状态。
   - 讨论中提到，GICv5 需要在虚拟化环境中进行特定的处理，以避免主机状态泄露给客体。

3. **本周的新讨论、进展或结论**：
   - 本周的补丁实现了 GICv5 的基本功能，包括 PPI 的直接注入、状态保存与恢复、以及对 ICC_IAFFIDR_EL1 寄存器的访问模拟。
   - 讨论中还提到，GICv5 不支持保护模式，相关功能在实现时被隐藏。
   - 还引入了对 GICv5 的自测试，确保其在基本单核虚拟机中的功能正常。
   - 通过补丁，KVM 的 IRQ 处理机制也进行了相应的调整，以支持 GICv5 的新特性。

总的来说，本周的讨论和补丁推进了 KVM 对 GICv5 的支持，尽管仍有一些功能（如对 SPI 的支持）待后续实现。

#### 📝 邮件列表

1. **[12-12 15:22]** [PATCH 00/32] KVM: arm64: Introduce vGIC-v5 with PPI support
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[12-12 15:22]** [PATCH 02/32] KVM: arm64: gic-v3: Switch vGIC-v3 to use generated
 ICH_VMCR_EL2
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
3. **[12-12 15:22]** [PATCH 01/32] KVM: arm64: Account for RES1 bits in DECLARE_FEAT_MAP()
 and co
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
4. **[12-12 15:22]** [PATCH 04/32] arm64/sysreg: Add remaining GICv5 ICC_ & ICH_ sysregs
 for KVM support
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
5. **[12-12 15:22]** [PATCH 03/32] arm64/sysreg: Drop ICH_HFGRTR_EL2.ICC_HAPR_EL1 and make
 RES1
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
6. **[12-12 15:22]** [PATCH 05/32] arm64/sysreg: Add GICR CDNMIA encoding
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
7. **[12-12 15:22]** [PATCH 08/32] KVM: arm64: gic-v5: Sanitize ID_AA64PFR2_EL1.GCIE
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
8. **[12-12 15:22]** [PATCH 07/32] KVM: arm64: gic: Introduce interrupt type helpers
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
9. **[12-12 15:22]** [PATCH 06/32] KVM: arm64: gic-v5: Add ARM_VGIC_V5 device to KVM
 headers
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
10. **[12-12 15:22]** [PATCH 09/32] KVM: arm64: gic-v5: Compute GICv5 FGTs on vcpu load
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
11. **[12-12 15:22]** [PATCH 10/32] KVM: arm64: gic-v5: Add emulation for ICC_IAFFID_EL1
 accesses
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
12. **[12-12 15:22]** [PATCH 13/32] KVM: arm64: gic-v5: Add vgic-v5 save/restore hyp
 interface
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
13. **[12-12 15:22]** [PATCH 11/32] KVM: arm64: gic-v5: Trap and emulate ICH_PPI_HMRx_EL1
 accesses
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
14. **[12-12 15:22]** [PATCH 12/32] KVM: arm64: gic: Set vgic_model before initing private
 IRQs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
15. **[12-12 15:22]** [PATCH 14/32] KVM: arm64: gic-v5: Implement GICv5 load/put and
 save/restore
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
16. **[12-12 15:22]** [PATCH 16/32] KVM: arm64: gic: Introduce irq_queue and
 set_pending_state to irq_ops
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
17. **[12-12 15:22]** [PATCH 15/32] KVM: arm64: gic-v5: Implement direct injection of PPIs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
18. **[12-12 15:22]** [PATCH 17/32] KVM: arm64: gic-v5: Implement PPI interrupt injection
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
19. **[12-12 15:22]** [PATCH 19/32] KVM: arm64: gic-v5: Init Private IRQs (PPIs) for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
20. **[12-12 15:22]** [PATCH 18/32] KVM: arm64: gic-v5: Check for pending PPIs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
21. **[12-12 15:22]** [PATCH 22/32] KVM: arm64: gic-v5: Reset vcpu state
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
22. **[12-12 15:22]** [PATCH 20/32] KVM: arm64: gic-v5: Support GICv5 interrupts with
 KVM_IRQ_LINE
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
23. **[12-12 15:22]** [PATCH 21/32] KVM: arm64: gic-v5: Create, init vgic_v5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
24. **[12-12 15:22]** [PATCH 23/32] KVM: arm64: gic-v5: Bump arch timer for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
25. **[12-12 15:22]** [PATCH 24/32] KVM: arm64: gic-v5: Mandate architected PPI for PMU
 emulation on GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
26. **[12-12 15:22]** [PATCH 27/32] KVM: arm64: gic-v5: Introduce kvm_arm_vgic_v5_ops and
 register them
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
27. **[12-12 15:22]** [PATCH 26/32] KVM: arm64: gic-v5: Hide FEAT_GCIE from NV GICv5 guests
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
28. **[12-12 15:22]** [PATCH 25/32] KVM: arm64: gic: Hide GICv5 for protected guests
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
29. **[12-12 15:22]** [PATCH 28/32] KVM: arm64: gic-v5: Set ICH_VCTLR_EL2.En on boot
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
30. **[12-12 15:22]** [PATCH 30/32] KVM: arm64: gic-v5: Probe for GICv5 device
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
31. **[12-12 15:22]** [PATCH 29/32] irqchip/gic-v5: Check if impl is virt capable
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
32. **[12-12 15:22]** [PATCH 32/32] KVM: arm64: selftests: Introduce a minimal GICv5 PPI
 selftest
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
33. **[12-12 15:22]** [PATCH 31/32] Documentation: KVM: Introduce documentation for VGICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
34. **[12-12 16:24]** Re: [PATCH 09/32] KVM: arm64: gic-v5: Compute GICv5 FGTs on vcpu load
   - 发件人: Marc Zyngier <maz@kernel.org>
35. **[12-13 13:59]** Re: [PATCH 14/32] KVM: arm64: gic-v5: Implement GICv5 load/put and
 save/restore
   - 发件人: kernel test robot <lkp@intel.com>
36. **[12-13 16:05]** Re: [PATCH 14/32] KVM: arm64: gic-v5: Implement GICv5 load/put and
 save/restore
   - 发件人: kernel test robot <lkp@intel.com>

---

### Thread 3: [PATCH v6 00/44] KVM: x86: Add support for mediated vPMUs

**📧 邮件数**: 25 | **👥 参与者**: 3 | **📅 开始时间**: Fri,  5 Dec 2025 16:16:36 -0800

#### 🤖 AI 总结

本邮件线程讨论了一个关于KVM（内核虚拟机）支持中介虚拟性能监控单元（vPMUs）的补丁系列。该补丁旨在改善KVM中虚拟机的性能监控能力，减少宿主机和虚拟机之间的资源竞争，从而提高虚拟机的性能。

在历史讨论中，补丁的背景和目的被阐述，主要包括通过提供新的API来创建和释放中介vPMUs，以避免当前通过宿主机性能事件模拟虚拟机PMCs所带来的性能损失。此外，补丁还涉及多个代码优化和功能增强，例如删除不必要的参数和简化MSR（模型特定寄存器）处理逻辑。

在本周的新讨论中，参与者对多个补丁进行了审查和确认，特别是对MSR处理的顺序和安全性进行了深入探讨。Dapeng Mi对多个补丁表示认可，并进行了测试，确认在Skylake和Sapphire Rapids服务器上没有发现问题。此外，Peter Zijlstra提出了一些代码实现上的对称性问题，并建议在补丁合并时进行相应的调整。总体来看，本周的讨论主要集中在补丁的审查、测试结果以及对代码实现细节的进一步完善上。

#### 📝 邮件列表

1. **[12-05 16:16]** [PATCH v6 00/44] KVM: x86: Add support for mediated vPMUs
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[12-05 16:16]** [PATCH v6 04/44] perf: Add APIs to create/release mediated guest vPMUs
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[12-05 16:17]** [PATCH v6 35/44] KVM: VMX: Drop intermediate "guest" field from msr_autostore
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[12-05 16:17]** [PATCH v6 37/44] KVM: VMX: Dedup code for removing MSR from VMCS's
 auto-load list
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[12-05 16:17]** [PATCH v6 38/44] KVM: VMX: Drop unused @entry_only param from add_atomic_switch_msr()
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[12-05 16:17]** [PATCH v6 39/44] KVM: VMX: Bug the VM if either MSR auto-load list is full
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[12-05 16:17]** [PATCH v6 40/44] KVM: VMX: Set MSR index auto-load entry if and only
 if entry is "new"
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[12-05 16:17]** [PATCH v6 41/44] KVM: VMX: Compartmentalize adding MSRs to host vs.
 guest auto-load list
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[12-05 16:17]** [PATCH v6 42/44] KVM: VMX: Dedup code for adding MSR to VMCS's auto list
   - 发件人: Sean Christopherson <seanjc@google.com>
10. **[12-05 16:17]** [PATCH v6 44/44] KVM: VMX: Add mediated PMU support for CPUs without
 "save perf global ctrl"
   - 发件人: Sean Christopherson <seanjc@google.com>
11. **[12-08 17:14]** Re: [PATCH v6 35/44] KVM: VMX: Drop intermediate "guest" field from
 msr_autostore
   - 发件人: Mi, Dapeng <dapeng1.mi@linux.intel.com>
12. **[12-08 17:29]** Re: [PATCH v6 37/44] KVM: VMX: Dedup code for removing MSR from
 VMCS's auto-load list
   - 发件人: Mi, Dapeng <dapeng1.mi@linux.intel.com>
13. **[12-08 17:32]** Re: [PATCH v6 38/44] KVM: VMX: Drop unused @entry_only param from
 add_atomic_switch_msr()
   - 发件人: Mi, Dapeng <dapeng1.mi@linux.intel.com>
14. **[12-08 17:32]** Re: [PATCH v6 39/44] KVM: VMX: Bug the VM if either MSR auto-load
 list is full
   - 发件人: Mi, Dapeng <dapeng1.mi@linux.intel.com>
15. **[12-08 17:34]** Re: [PATCH v6 39/44] KVM: VMX: Bug the VM if either MSR auto-load
 list is full
   - 发件人: Mi, Dapeng <dapeng1.mi@linux.intel.com>
16. **[12-08 17:35]** Re: [PATCH v6 40/44] KVM: VMX: Set MSR index auto-load entry if and
 only if entry is "new"
   - 发件人: Mi, Dapeng <dapeng1.mi@linux.intel.com>
17. **[12-08 17:36]** Re: [PATCH v6 41/44] KVM: VMX: Compartmentalize adding MSRs to host
 vs. guest auto-load list
   - 发件人: Mi, Dapeng <dapeng1.mi@linux.intel.com>
18. **[12-08 17:37]** Re: [PATCH v6 42/44] KVM: VMX: Dedup code for adding MSR to VMCS's
 auto list
   - 发件人: Mi, Dapeng <dapeng1.mi@linux.intel.com>
19. **[12-08 17:39]** Re: [PATCH v6 44/44] KVM: VMX: Add mediated PMU support for CPUs
 without "save perf global ctrl"
   - 发件人: Mi, Dapeng <dapeng1.mi@linux.intel.com>
20. **[12-08 12:51]** Re: [PATCH v6 04/44] perf: Add APIs to create/release mediated guest
 vPMUs
   - 发件人: Peter Zijlstra <peterz@infradead.org>
21. **[12-08 16:37]** Re: [PATCH v6 00/44] KVM: x86: Add support for mediated vPMUs
   - 发件人: Peter Zijlstra <peterz@infradead.org>
22. **[12-08 10:07]** Re: [PATCH v6 04/44] perf: Add APIs to create/release mediated guest vPMUs
   - 发件人: Sean Christopherson <seanjc@google.com>
23. **[12-09 14:31]** Re: [PATCH v6 44/44] KVM: VMX: Add mediated PMU support for CPUs
 without "save perf global ctrl"
   - 发件人: Mi, Dapeng <dapeng1.mi@linux.intel.com>
24. **[12-09 09:37]** Re: [PATCH v6 37/44] KVM: VMX: Dedup code for removing MSR from
 VMCS's auto-load list
   - 发件人: Sean Christopherson <seanjc@google.com>
25. **[12-10 09:08]** Re: [PATCH v6 37/44] KVM: VMX: Dedup code for removing MSR from
 VMCS's auto-load list
   - 发件人: Mi, Dapeng <dapeng1.mi@linux.intel.com>

---

### Thread 4: [PATCH v2 0/6] KVM: arm64: VTCR_EL2 conversion to feature dependency framework

**📧 邮件数**: 19 | **👥 参与者**: 4 | **📅 开始时间**: Wed, 10 Dec 2025 17:30:18 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 VTCR_EL2 寄存器转换为特性依赖框架的补丁系列（PATCH v2 0/6）。该系列补丁主要目的是改进 VTCR_EL2 的处理，确保其与其他特性之间的依赖关系得到正确管理。

在历史讨论中，Marc Zyngier 提出了对 VTCR_EL2 的清理和简化，强调了处理 RES1 位的重要性，并修复了与 FEAT_XNX 相关的问题。补丁还扩展了 DECLARE_FEAT_MAP() 的处理范围，以适应新的 GICv5 特性。

在本周的新讨论中，Marc 提交了六个补丁，涵盖了多个方面的改进：
1. 修复了 EL2 S1 XN 处理，确保在 hVHE 设置下的正确性。
2. 将 ID_AA64MMFR0_EL1.TGRAN{4,16,64}_2 转换为无序枚举。
3. 将 VTCR_EL2 转换为系统寄存器基础设施，确保定义的一致性。
4. 考虑 RES1 位在 DECLARE_FEAT_MAP() 中的处理。
5. 实现 VTCR_EL2 的配置驱动清理。
6. 处理 EL2 S1 映射的 UX/PX 属性。

本周的讨论中，参与者对补丁进行了审查并提出了一些小的修改建议，整体上得到了积极的反馈，部分补丁已被确认可以合并。整体来看，这一系列补丁旨在提升 KVM 在 arm64 架构下的稳定性和性能。

#### 📝 邮件列表

1. **[12-10 17:30]** [PATCH v2 0/6] KVM: arm64: VTCR_EL2 conversion to feature dependency framework
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[12-10 17:30]** [PATCH v2 1/6] KVM: arm64: Fix EL2 S1 XN handling for hVHE setups
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[12-10 17:30]** [PATCH v2 2/6] arm64: Convert ID_AA64MMFR0_EL1.TGRAN{4,16,64}_2 to UnsignedEnum
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[12-10 17:30]** [PATCH v2 3/6] arm64: Convert VTCR_EL2 to sysreg infratructure
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[12-10 17:30]** [PATCH v2 4/6] KVM: arm64: Account for RES1 bits in DECLARE_FEAT_MAP() and co
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[12-10 17:30]** [PATCH v2 5/6] KVM: arm64: Convert VTCR_EL2 to config-driven sanitisation
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[12-10 17:30]** [PATCH v2 6/6] KVM: arm64: Honor UX/PX attributes for EL2 S1 mappings
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[12-11 13:37]** Re: [PATCH v2 1/6] KVM: arm64: Fix EL2 S1 XN handling for hVHE setups
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[12-11 13:38]** Re: [PATCH v2 2/6] arm64: Convert ID_AA64MMFR0_EL1.TGRAN{4,16,64}_2
 to UnsignedEnum
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[12-11 14:13]** Re: [PATCH v2 3/6] arm64: Convert VTCR_EL2 to sysreg infratructure
   - 发件人: Fuad Tabba <tabba@google.com>
11. **[12-11 14:30]** Re: [PATCH v2 4/6] KVM: arm64: Account for RES1 bits in
 DECLARE_FEAT_MAP() and co
   - 发件人: Fuad Tabba <tabba@google.com>
12. **[12-11 14:30]** Re: [PATCH v2 1/6] KVM: arm64: Fix EL2 S1 XN handling for hVHE setups
   - 发件人: Marc Zyngier <maz@kernel.org>
13. **[12-11 14:44]** Re: [PATCH v2 5/6] KVM: arm64: Convert VTCR_EL2 to config-driven sanitisation
   - 发件人: Fuad Tabba <tabba@google.com>
14. **[12-11 14:51]** Re: [PATCH v2 6/6] KVM: arm64: Honor UX/PX attributes for EL2 S1 mappings
   - 发件人: Fuad Tabba <tabba@google.com>
15. **[12-11 14:55]** Re: [PATCH v2 0/6] KVM: arm64: VTCR_EL2 conversion to feature
 dependency framework
   - 发件人: Fuad Tabba <tabba@google.com>
16. **[12-11 15:18]** Re: [PATCH v2 6/6] KVM: arm64: Honor UX/PX attributes for EL2 S1
 mappings
   - 发件人: Joey Gouly <joey.gouly@arm.com>
17. **[12-11 16:21]** Re: [PATCH v2 6/6] KVM: arm64: Honor UX/PX attributes for EL2 S1 mappings
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[12-11 17:23]** Re: [PATCH v2 4/6] KVM: arm64: Account for RES1 bits in
 DECLARE_FEAT_MAP() and co
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
19. **[12-12 16:00]** Re: [PATCH v2 6/6] KVM: arm64: Honor UX/PX attributes for EL2 S1
 mappings
   - 发件人: Joey Gouly <joey.gouly@arm.com>

---

### Thread 5: [PATCH 1/2] KVM: arm64: gic: Enable GICv3 CPUIF trapping on GICv5
 hosts if required

**📧 邮件数**: 14 | **👥 参与者**: 5 | **📅 开始时间**: Mon, 8 Dec 2025 15:28:22 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构上 GIC（Generic Interrupt Controller）相关的两个补丁。

1. **原始补丁内容**：
   - 第一个补丁（[PATCH 1/2]）旨在为 GICv5 主机启用 GICv3 CPUIF（CPU接口）陷阱，以确保在 GICv5 主机上正确处理 GICv3 CPUIF 陷阱，避免向来宾注入未定义的指令。

2. **之前讨论要点**：
   - 之前的讨论主要集中在如何处理 GICv3 和 GICv5 之间的兼容性问题，尤其是在 GICv5 主机上运行 GICv3 来宾时，确保陷阱能够正确触发并被 KVM 处理。

3. **本周新讨论与进展**：
   - 本周的讨论中，Sascha Bischoff 提出了两个补丁，分别是启用 GICv3 CPUIF 陷阱和修复 ICH_HCR_EL2_TDIR 能力测试的顺序问题，以确保在 GICv5 主机上能够正确识别和处理 GICv3 CPUIF 支持。
   - 参与者对补丁进行了审核，Marc Zyngier 表示支持，并确认了补丁的有效性。Alexandru Elisei 还提出了与 pKVM 相关的修复，确保在加载 VCPU 时正确复制 FGT 陷阱配置。
   - 整体来看，本周的讨论推动了对 GICv5 和 GICv3 兼容性问题的解决，并得到了社区成员的积极反馈和支持。

#### 📝 邮件列表

1. **[12-08 15:28]** [PATCH 1/2] KVM: arm64: gic: Enable GICv3 CPUIF trapping on GICv5
 hosts if required
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[12-08 15:28]** [PATCH 0/2] Enable GICv5 Legacy CPUIF trapping & fix TDIR cap test
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
3. **[12-08 15:28]** [PATCH 0/2] Enable GICv5 Legacy CPUIF trapping & fix TDIR cap test
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
4. **[12-08 15:28]** [PATCH 2/2] KVM: arm64: Correct test for ICH_HCR_EL2_TDIR cap for
 GICv5 hosts
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
5. **[12-08 15:53]** Re: [PATCH 0/2] Enable GICv5 Legacy CPUIF trapping & fix TDIR cap test
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[12-10 13:21]** [PATCH 0/2] KVM: arm64: pKVM fixes
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
7. **[12-10 13:21]** [PATCH 1/2] KVM: arm64: Copy FGT traps to unprotected pKVM VCPU on VCPU load
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
8. **[12-10 13:21]** [PATCH 2/2] KVM: arm64: Remove extra argument for __pvkm_host_{share,unshare}_hyp()
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
9. **[12-11 08:15]** Re: [PATCH 2/2] KVM: arm64: Remove extra argument for __pvkm_host_{share,unshare}_hyp()
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[12-11 09:33]** Re: [PATCH 2/2] KVM: arm64: Remove extra argument for
 __pvkm_host_{share,unshare}_hyp()
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
11. **[12-11 11:57]** Re: [PATCH 2/2] KVM: arm64: Remove extra argument for __pvkm_host_{share,unshare}_hyp()
   - 发件人: Marc Zyngier <maz@kernel.org>
12. **[12-12 05:36]** Re: [PATCH 1/2] KVM: arm64: Copy FGT traps to unprotected pKVM VCPU
 on VCPU load
   - 发件人: Will Deacon <will@kernel.org>
13. **[12-12 08:04]** Re: [PATCH 1/2] KVM: arm64: Copy FGT traps to unprotected pKVM VCPU
 on VCPU load
   - 发件人: Fuad Tabba <tabba@google.com>
14. **[12-12 10:30]** Re: [PATCH 1/2] KVM: arm64: Copy FGT traps to unprotected pKVM VCPU
 on VCPU load
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

### Thread 6: [PATCH v5 04/27] iommu/io-pgtable-arm: Factor kernel specific
 code out

**📧 邮件数**: 12 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 28 Nov 2025 12:45:41 -0400

#### 🤖 AI 总结

本邮件线程讨论了一个关于 Linux 内核中 IOMMU（输入输出内存管理单元）和 ARM 虚拟化的补丁，主题为“[PATCH v5 04/27] iommu/io-pgtable-arm: Factor kernel specific code out”。该补丁旨在将内核特定的代码抽象出来，以便更好地支持虚拟化环境。

在历史讨论中，参与者 Mostafa Saleh 提出了将 IOMMU 页码 API 提供给虚拟机监控器（hypervisor）的建议，并讨论了如何将现有的代码结构进行优化，以便在未来的驱动程序中更好地复用。此外，Jason Gunthorpe 对代码的组织提出了改进意见，建议将一些内联代码移至公共头文件，以提高可读性。

在本周的新讨论中，Mostafa Saleh 提到将大部分代码从 io-pgtable-arm 复用，并计划支持共享 CPU 的二级页表，这将涉及对核心虚拟机监控器代码的修改。他还表示希望保持当前补丁系列的简洁性，未来再进行优化和改进。此外，讨论中提到对 SMMU 嵌套支持的处理，Mostafa 计划在后续版本中进一步完善相关功能。

总体来看，讨论集中在如何优化 IOMMU 驱动程序的结构和功能，以支持更复杂的虚拟化需求，同时确保代码的可维护性和清晰性。

#### 📝 邮件列表

1. **[11-28 12:45]** Re: [PATCH v5 04/27] iommu/io-pgtable-arm: Factor kernel specific
 code out
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
2. **[11-28 12:46]** Re: [PATCH v5 05/27] iommu/arm-smmu-v3: Split code with hyp
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
3. **[11-28 12:48]** Re: [PATCH v5 07/27] iommu/arm-smmu-v3: Move IDR parsing to common
 functions
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
4. **[11-28 12:56]** Re: [PATCH v5 14/27] iommu/arm-smmu-v3: Support probing KVM emulated
 devices
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
5. **[11-28 13:07]** Re: [PATCH v5 17/27] iommu/arm-smmu-v3-kvm: Probe SMMU HW
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
6. **[11-28 13:12]** Re: [PATCH v5 27/27] iommu/arm-smmu-v3-kvm: Enable nesting
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
7. **[12-12 15:37]** Re: [PATCH v5 04/27] iommu/io-pgtable-arm: Factor kernel specific
 code out
   - 发件人: Mostafa Saleh <smostafa@google.com>
8. **[12-12 15:41]** Re: [PATCH v5 05/27] iommu/arm-smmu-v3: Split code with hyp
   - 发件人: Mostafa Saleh <smostafa@google.com>
9. **[12-12 15:42]** Re: [PATCH v5 07/27] iommu/arm-smmu-v3: Move IDR parsing to common
 functions
   - 发件人: Mostafa Saleh <smostafa@google.com>
10. **[12-12 15:53]** Re: [PATCH v5 14/27] iommu/arm-smmu-v3: Support probing KVM emulated
 devices
   - 发件人: Mostafa Saleh <smostafa@google.com>
11. **[12-12 16:07]** Re: [PATCH v5 17/27] iommu/arm-smmu-v3-kvm: Probe SMMU HW
   - 发件人: Mostafa Saleh <smostafa@google.com>
12. **[12-12 16:15]** Re: [PATCH v5 27/27] iommu/arm-smmu-v3-kvm: Enable nesting
   - 发件人: Mostafa Saleh <smostafa@google.com>

---

### Thread 7: [PATCH v11 RESEND 0/9] support FEAT_LSUI

**📧 邮件数**: 10 | **👥 参与者**: 1 | **📅 开始时间**: Sun, 14 Dec 2025 11:22:39 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是支持 Armv9.6 的 FEAT_LSUI 特性，主要涉及对 Linux 内核中相关功能的补丁集（PATCH v11 RESEND 0/9）。

1. **原始 patch/问题的内容**：
   FEAT_LSUI 提供了特权级代码访问用户内存的加载/存储指令，而无需清除 PSTATE.PAN 位。此补丁集旨在支持 FEAT_LSUI，并在 futex 原子操作和用户 swpX 模拟中替换掉需要清除 PSTATE.PAN 位的实现。

2. **之前的讨论要点**：
   在历史版本中，补丁经历了多次重构和调整，逐步完善了对 FEAT_LSUI 的支持，包括对用户 swpX 模拟的应用、测试覆盖的增加以及对相关 Kconfig 的配置。

3. **本周的新讨论、进展或结论**：
   本周的讨论集中在补丁的具体实现上，包括：
   - 添加了对 FEAT_LSUI 的 CPU 特性检测。
   - 将 FEAT_LSUI 暴露给虚拟机（KVM）。
   - 增加了对 FEAT_LSUI 的测试覆盖。
   - 更新了 Kconfig，以检测工具链对 LSUI 的支持。
   - 重构了 futex 原子操作，以便在支持 FEAT_LSUI 时不再清除 PSTATE.PAN。
   - 将相关的 LSUI 定义分离到新的头文件 lsui.h 中，以便复用。
   - 将 user_swpX 宏转换为内联函数，以便于应用 FEAT_LSUI。

这些进展表明补丁集正在逐步完善，预计将为 Linux 内核带来更高效的用户内存访问能力。

#### 📝 邮件列表

1. **[12-14 11:22]** [PATCH v11 RESEND 0/9] support FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[12-14 11:22]** [PATCH v11 RESEND 1/9] arm64: cpufeature: add FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[12-14 11:22]** [PATCH v11 RESEND 2/9] KVM: arm64: expose FEAT_LSUI to guest
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
4. **[12-14 11:22]** [PATCH v11 RESEND 3/9] KVM: arm64: kselftest: set_id_regs: add test for FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
5. **[12-14 11:22]** [PATCH v11 RESEND 4/9] arm64: Kconfig: Detect toolchain support for LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
6. **[12-14 11:22]** [PATCH v11 RESEND 5/9] arm64: futex: refactor futex atomic operation
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
7. **[12-14 11:22]** [PATCH v11 RESEND 6/9] arm64: futex: support futex with FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
8. **[12-14 11:22]** [PATCH v11 RESEND 7/9] arm64: separate common LSUI definitions into lsui.h
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
9. **[12-14 11:22]** [PATCH v11 RESEND 8/9] arm64: armv8_deprecated: convert user_swpX to inline function
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
10. **[12-14 11:22]** [PATCH v11 RESEND 9/9] arm64: armv8_deprecated: apply FEAT_LSUI for swpX emulation.
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 8: [PATCH v6 0/9] KVM: arm64: Fixes for guest CPU feature trapping and enabling

**📧 邮件数**: 10 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 11 Dec 2025 10:47:00 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的修复补丁，主要集中在来宾 CPU 特性捕获和启用的问题上。

1. **原始补丁内容**：本次补丁系列（PATCH v6 0/9）包含多个修复，旨在解决 pKVM（Protected KVM）中来宾特性捕获和启用的相关问题，同时进行了一些代码整理。补丁基于 Linux 6.18 版本。

2. **之前讨论要点**：虽然没有具体的历史讨论记录，但补丁的提出显然是为了修复之前版本中存在的特性捕获和启用逻辑错误，确保在受保护的虚拟机中正确处理 CPU 特性。

3. **本周的新讨论与进展**：本周的讨论中，Fuad Tabba 提出了多个补丁的详细说明，包括：
   - 修复 Trace Buffer 捕获逻辑，确保在不支持该特性的情况下能正确捕获相关寄存器。
   - 修复 MTE（Memory Tagging Extension）标志的初始化逻辑，确保仅在允许的情况下设置该标志。
   - 引入新的辅助函数来计算故障 IPA（Intermediate Physical Address）偏移，并优化代码可读性。
   - 扩展 pKVM 能力检查，确保根据虚拟机类型正确判断支持的特性。
   - 禁止在受保护模式下为任何虚拟机启用 MTE，以减少复杂性。
   - 追踪 KVM IOCTL 及其相关能力，以便在 CoCo VM Hypervisors 中判断特定 IOCTL 是否被允许。

整体来看，本周的讨论集中在确保 KVM 在处理受保护虚拟机时的稳定性和正确性上，修复了多个潜在问题，并对代码进行了优化。

#### 📝 邮件列表

1. **[12-11 10:47]** [PATCH v6 0/9] KVM: arm64: Fixes for guest CPU feature trapping and enabling
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[12-11 10:47]** [PATCH v6 1/9] KVM: arm64: Fix Trace Buffer trapping for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[12-11 10:47]** [PATCH v6 2/9] KVM: arm64: Fix Trace Buffer trap polarity for
 protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[12-11 10:47]** [PATCH v6 3/9] KVM: arm64: Fix MTE flag initialization for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[12-11 10:47]** [PATCH v6 4/9] KVM: arm64: Introduce helper to calculate fault IPA offset
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[12-11 10:47]** [PATCH v6 5/9] KVM: arm64: Include VM type when checking VM
 capabilities in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[12-11 10:47]** [PATCH v6 6/9] KVM: arm64: Do not allow KVM_CAP_ARM_MTE for any guest
 in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[12-11 10:47]** [PATCH v6 7/9] KVM: arm64: Track KVM IOCTLs and their associated KVM caps
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[12-11 10:47]** [PATCH v6 8/9] KVM: arm64: Check whether a VM IOCTL is allowed in pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
10. **[12-11 10:47]** [PATCH v6 9/9] KVM: arm64: Prevent host from managing timer offsets
 for protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 9: [PATCH v8 00/13] Direct Map Removal Support for guest_memfd

**📧 邮件数**: 9 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 5 Dec 2025 16:57:45 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对虚拟机内存的直接映射移除支持的补丁（PATCH v8 00/13），旨在缓解Spectre等瞬态执行问题。补丁的核心是通过在内核页表中不包含指向虚拟机内存的条目，来防止潜在的安全漏洞。

在历史讨论中，参与者们探讨了几个补丁的具体实现，包括引入AS_NO_DIRECT_MAP标志以标识不应直接映射的内存，以及为KVM创建的guest_memfd添加移除直接映射的标志（GUEST_MEMFD_FLAG_NO_DIRECT_MAP）。这些补丁的目的是确保在处理虚拟机内存时，内核能够有效地管理和保护这些内存区域。

在本周的新讨论中，Vlastimil Babka提出了对补丁的具体实现细节的关注，特别是关于如何在直接映射的清除和TLB刷新之间设置标志的问题。他指出，如果在未来再次调用kvm_gmem_folio_zap_direct_map()，可能会因为未清除标志而导致无效操作。此外，Babka还确认了对AS_NO_DIRECT_MAP补丁的认可，并讨论了将gup更改分离的必要性，以确保逻辑上的一致性。

总体而言，讨论围绕如何更好地实现和验证这些补丁的有效性与安全性展开，参与者们积极提供反馈和建议。

#### 📝 邮件列表

1. **[12-05 16:57]** [PATCH v8 00/13] Direct Map Removal Support for guest_memfd
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
2. **[12-05 16:58]** [PATCH v8 03/13] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
3. **[12-05 16:58]** [PATCH v8 04/13] KVM: guest_memfd: Add stub for
 kvm_arch_gmem_invalidate
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
4. **[12-05 16:58]** [PATCH v8 05/13] KVM: guest_memfd: Add flag to remove from direct map
   - 发件人: Kalyazin, Nikita <kalyazin@amazon.co.uk>
5. **[12-05 10:35]** Re: [PATCH v8 03/13] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: John Hubbard <jhubbard@nvidia.com>
6. **[12-08 09:43]** Re: [PATCH v8 05/13] KVM: guest_memfd: Add flag to remove from direct
 map
   - 发件人: Vlastimil Babka <vbabka@suse.cz>
7. **[12-08 10:00]** Re: [PATCH v8 03/13] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Vlastimil Babka <vbabka@suse.cz>
8. **[12-08 10:02]** Re: [PATCH v8 03/13] mm: introduce AS_NO_DIRECT_MAP
   - 发件人: Vlastimil Babka <vbabka@suse.cz>
9. **[12-08 10:10]** Re: [PATCH v8 04/13] KVM: guest_memfd: Add stub for
 kvm_arch_gmem_invalidate
   - 发件人: Vlastimil Babka <vbabka@suse.cz>

---

### Thread 10: [PATCH v2 0/5] KVM: arm64: Enforce MTE disablement at EL2

**📧 邮件数**: 6 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 11 Dec 2025 11:38:23 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM (Kernel-based Virtual Machine) 中强制在 EL2 级别禁用 MTE (Memory Tagging Extension)。Fuad Tabba 提出了一个包含五个补丁的系列，目的是确保即使在硬件支持 MTE 的情况下，恶意主机也无法利用 MTE 来攻击虚拟机或超管。

**原始补丁内容**：
补丁的核心在于，当主机禁用 MTE 时，通过清除 HCR_EL2.ATA 来显式禁用 MTE。这一措施确保任何 MTE 指令的使用都会导致数据中止（Data Abort），从而保护超管和虚拟机的安全。

**之前讨论要点**：
历史讨论中没有具体提及，但补丁的背景是为了防止恶意主机利用 MTE 指令访问虚拟机的内存标签，造成潜在的安全风险。

**本周新讨论与进展**：
本周的讨论主要集中在补丁的具体实现上，包括：
1. 移除与 pKVM 相关的死代码。
2. 清除 HCR_EL2.ATA 以防止 MTE 指令的执行。
3. 重构异常处理逻辑，以便在 MTE 被禁用时能正确注入未定义指令异常。
4. 在访问 MTE 系统寄存器时注入未定义指令异常，以更好地模拟不支持 MTE 的硬件。
5. 在 pKVM 初始化 HCR 陷阱时，使用 kvm_has_mte() 进行更全面的 MTE 支持检查。

这些补丁的实施将增强 KVM 的安全性，确保在 MTE 被禁用时，系统的行为符合预期。

#### 📝 邮件列表

1. **[12-11 11:38]** [PATCH v2 0/5] KVM: arm64: Enforce MTE disablement at EL2
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[12-11 11:38]** [PATCH v2 1/5] arm64: Remove dead code resetting HCR_EL2 for pKVM
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[12-11 11:38]** [PATCH v2 2/5] arm64: Clear HCR_EL2.ATA when MTE is not supported or disabled
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[12-11 11:38]** [PATCH v2 3/5] KVM: arm64: Refactor enter_exception64()
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[12-11 11:38]** [PATCH v2 4/5] arm64: Inject UNDEF when accessing MTE sysregs with
 MTE disabled
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[12-11 11:38]** [PATCH v2 5/5] KVM: arm64: Use kvm_has_mte() in pKVM trap initialization
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 11: [PATCH v4 2/3] KVM: selftests: Test for KVM_EXIT_ARM_SEA

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 11 Dec 2025 21:02:27 +0800

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM 的自测试补丁，主题为“[PATCH v4 2/3] KVM: selftests: Test for KVM_EXIT_ARM_SEA”。该补丁旨在测试 KVM 在 ARM 架构下处理特定异常（SEA，System Error Abort）的能力。

在历史讨论中，参与者们并未提供具体的背景信息，但本周的新讨论中，Zenghui Yu 和 Jiaqi Yan 就补丁的测试过程中遇到的问题进行了深入交流。Zenghui 提到在不同服务器上测试时遇到了一些问题，包括 ASSERT 失败，怀疑 KVM 在注入错误时未能正确模拟某些情况。Jiaqi 也确认了测试中可能遗漏的部分，并提出了改进建议，包括在无法访问必要文件时提前返回以跳过测试。

本周的进展包括 Jiaqi 提出了一些修复措施，特别是针对未处理的 GUEST_FAIL 错误，建议在测试代码中进行重构以提高稳定性。此外，他还分享了一个修复补丁，改进了测试逻辑，确保在特定条件下能够正确处理 KVM 的退出原因，并在必要时返回 KSFT_SKIP 或 KSFT_FAIL。

总的来说，本周的讨论集中在补丁的测试问题及其改进上，参与者们积极探讨解决方案，以确保 KVM 在 ARM 架构下的异常处理能力得到验证。

#### 📝 邮件列表

1. **[12-11 21:02]** Re: [PATCH v4 2/3] KVM: selftests: Test for KVM_EXIT_ARM_SEA
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>
2. **[12-11 17:53]** Re: [PATCH v4 2/3] KVM: selftests: Test for KVM_EXIT_ARM_SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
3. **[12-12 17:21]** Re: [PATCH v4 2/3] KVM: selftests: Test for KVM_EXIT_ARM_SEA
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>
4. **[12-12 14:42]** Re: [PATCH v4 2/3] KVM: selftests: Test for KVM_EXIT_ARM_SEA
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>

---

### Thread 12: [PATCH] KVM: Remove subtle "struct kvm_stats_desc" pseudo-overlay

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Fri,  5 Dec 2025 15:26:55 -0800

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM 的补丁，主题为“移除微妙的 `struct kvm_stats_desc` 伪覆盖”。该补丁的目的是去除 KVM 内部对 `kvm_stats_desc` 的伪覆盖，解决由于灵活数组成员位置不当而引发的编译器警告，并简化 KVM 的解引用过程。补丁建议在构建内核时将用户API结构定义为固定大小的名称，从而避免这种覆盖。

在历史讨论中，Sean Christopherson 提出了这个补丁，并详细说明了其必要性和预期效果。补丁还顺便清理了统计宏的缩进。

在本周的新讨论中，Christian Borntraeger 和 Marc Zyngier 对该补丁表示认可，均已给予“确认通过”（Acked-by），表明他们支持这一改动。Christian 提到是否需要额外的注释，认为可能使用 git blame 足以追踪变更。整体来看，本周的讨论主要集中在对补丁的认可与确认上，未提出新的问题或异议。

#### 📝 邮件列表

1. **[12-05 15:26]** [PATCH] KVM: Remove subtle "struct kvm_stats_desc" pseudo-overlay
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[12-08 11:32]** Re: [PATCH] KVM: Remove subtle "struct kvm_stats_desc" pseudo-overlay
   - 发件人: Christian Borntraeger <borntraeger@linux.ibm.com>
3. **[12-08 10:42]** Re: [PATCH] KVM: Remove subtle "struct kvm_stats_desc" pseudo-overlay
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 13: [PATCH] KVM: arm64: vgic: simplify vgic_v3_redist_region_full()

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 11 Dec 2025 23:51:09 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的虚拟中断控制器（vgic）相关的补丁，旨在简化 `vgic_v3_redist_region_full()` 函数的实现。

**原始补丁内容**：补丁由 Osama Abdelkader 提交，主要通过将原有的 if-return-false 模式转换为直接的布尔表达式返回，来使代码更加简洁和可读。具体修改涉及到 `vgic.h` 文件中的 `vgic_v3_redist_region_full()` 函数。

**之前的讨论要点**：本线程没有历史讨论，所有讨论均为本周的新进展。

**本周的新讨论与进展**：在本周的讨论中，Marc Zyngier 对补丁提出了质疑，认为简化后的代码并不更清晰，特别是检查为零的条件是重要的，应该作为单独的语句来处理。他建议停止提交仅仅是为了个人风格调整的补丁，认为有更多实际问题需要解决，建议将时间投入到更有意义的补丁审查中。

总结来看，本周的讨论主要集中在代码可读性和补丁的实际价值上，Marc Zyngier 对补丁提出了反对意见，强调了代码逻辑的重要性。

#### 📝 邮件列表

1. **[12-11 23:51]** [PATCH] KVM: arm64: vgic: simplify vgic_v3_redist_region_full()
   - 发件人: Osama Abdelkader <osama.abdelkader@gmail.com>
2. **[12-12 09:35]** Re: [PATCH] KVM: arm64: vgic: simplify vgic_v3_redist_region_full()
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 14: [PATCH] KVM: arm64: vgic: add default case to switch statement

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 11 Dec 2025 23:40:28 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 vgic（虚拟通用中断控制器）代码中的一个补丁。补丁的内容是向 `vgic_validate_injection()` 函数中的 switch 语句添加一个默认情况，以增强代码的防御性。

在历史讨论中，补丁的作者 Osama Abdelkader 提出了这个补丁，认为在处理 `irq->config` 的所有枚举值时，缺少默认情况可能会导致潜在的问题，因此希望通过添加默认情况来提高代码的健壮性。

本周的新讨论中，Marc Zyngier 对补丁提出了质疑。他指出，实际上该文件中只有这个 switch 语句，并且 enum 类型 `vgic_irq_config` 仅包含两个值（边缘触发和电平触发），因此 switch 语句已经覆盖了所有可能的情况。他认为添加默认情况并没有实际意义，反而建议删除最后的返回语句，因为它是多余的。Marc 对补丁的必要性表示怀疑，并建议补丁作者在提交补丁前仔细审查代码，以避免浪费他人时间。

总结来看，本周的讨论主要集中在补丁的合理性和必要性上，Marc 提出的观点引发了对代码覆盖性和补丁有效性的深入思考。

#### 📝 邮件列表

1. **[12-11 23:40]** [PATCH] KVM: arm64: vgic: add default case to switch statement
   - 发件人: Osama Abdelkader <osama.abdelkader@gmail.com>
2. **[12-12 09:28]** Re: [PATCH] KVM: arm64: vgic: add default case to switch statement
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 RFC

共 3 个 thread

---

### Thread 1: [RFC PATCH v6 00/35] KVM: arm64: Add Statistical Profiling
 Extension (SPE) support

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 11 Dec 2025 16:34:25 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM（Kernel-based Virtual Machine）中为 ARM64 架构添加统计分析扩展（SPE）支持的 RFC PATCH v6。该补丁旨在增强 KVM 对 SPE 的虚拟化支持，涉及内存管理和中断处理等多个技术细节。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的提出是为了改进 KVM 对 SPE 的支持，尤其是在虚拟化环境下的内存分配和管理方面。

本周的讨论主要集中在 Leo Yan 和 Alexandru Elisei 之间的技术问答。Leo 提出了对补丁中“在第二阶段固定内存”的理解问题，并讨论了 KVM 如何处理虚拟地址到物理地址的映射。他指出，KVM 需要在启用 SPE 之前为跟踪缓冲区分配内存，并确保相关的物理页面在会话期间被固定。Alexandr 对此进行了澄清，强调 KVM 在管理第二阶段表时不需要将这些页面映射到用户空间，并解释了如何处理数据中断和缓冲区管理事件。

总结来看，本周的讨论加深了对补丁实现细节的理解，特别是在内存管理和中断处理方面，双方的交流为后续补丁的完善提供了重要的技术支持。

#### 📝 邮件列表

1. **[12-11 16:34]** Re: [RFC PATCH v6 00/35] KVM: arm64: Add Statistical Profiling
 Extension (SPE) support
   - 发件人: Leo Yan <leo.yan@arm.com>
2. **[12-12 10:18]** Re: [RFC PATCH v6 00/35] KVM: arm64: Add Statistical Profiling
 Extension (SPE) support
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
3. **[12-12 11:15]** Re: [RFC PATCH v6 00/35] KVM: arm64: Add Statistical Profiling
 Extension (SPE) support
   - 发件人: Leo Yan <leo.yan@arm.com>
4. **[12-12 11:54]** Re: [RFC PATCH v6 00/35] KVM: arm64: Add Statistical Profiling
 Extension (SPE) support
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

### Thread 2: [RFC PATCH v6 01/35] arm64/sysreg: Add new SPE fields

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 10 Dec 2025 18:38:27 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于一个针对 ARM64 系统寄存器的新补丁（patch），具体内容为增加新的 SPE 字段。该补丁旨在改进 ARM64 架构中对系统寄存器的支持，尤其是在处理虚拟地址和物理地址时的灵活性。

在历史讨论中，虽然没有提供具体的上下文，但可以推测该补丁的提出是为了优化现有的地址模式定义。参与者们对枚举名称的选择进行了讨论，认为现有名称与定义不太匹配。

在本周的新讨论中，参与者 Leo Yan 提出了对枚举名称的建议，特别是对地址模式的命名提出了修改意见。他建议将某个值命名为 "VA_PA"（虚拟和物理地址支持），并对其他值的命名进行了讨论。Alexandru Elisei 对此表示认可，并进一步建议将最后一个值命名为 "PA_ONLY"（仅物理地址）。这表明参与者们在积极协作，致力于确保补丁的准确性和一致性。整体来看，讨论围绕着如何更好地定义和命名这些新字段，以提高代码的可读性和可维护性。

#### 📝 邮件列表

1. **[12-10 18:38]** Re: [RFC PATCH v6 01/35] arm64/sysreg: Add new SPE fields
   - 发件人: Leo Yan <leo.yan@arm.com>
2. **[12-12 09:39]** Re: [RFC PATCH v6 01/35] arm64/sysreg: Add new SPE fields
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

### Thread 3: [RFC PATCH v6 05/35] KVM: arm64: Add KVM_CAP_ARM_SPE capability

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Sun, 14 Dec 2025 20:18:42 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于在 KVM（Kernel-based Virtual Machine）中为 arm64 架构添加 KVM_CAP_ARM_SPE 能力的补丁（patch）。该补丁旨在增强 KVM 对 ARM 处理器的支持，特别是与性能监控单元（PMU）相关的功能。

在历史讨论中，虽然没有具体的邮件记录，但可以推测出该补丁的提出是为了引入对 ARM SPE（Statistical Profiling Extension）的支持，以提高虚拟化环境下的性能监控能力。

在本周的新讨论中，参与者 Leo Yan 提出了一个建议，认为可以通过检查 `list_empty(&arm_spus)` 来简化 KVM 中对 SPE 支持的实现，从而不再需要使用静态键 `kvm_spe_available`。他指出，这种做法不仅简化了代码，还与 CPU PMU 的虚拟化实现保持一致。这一建议可能会推动补丁的进一步优化和完善。

总的来说，本周的讨论集中在如何优化补丁的实现细节上，反映出对代码简洁性和一致性的关注。

#### 📝 邮件列表

1. **[12-14 20:18]** Re: [RFC PATCH v6 05/35] KVM: arm64: Add KVM_CAP_ARM_SPE capability
   - 发件人: Leo Yan <leo.yan@linux.dev>

---

## 📌 Bug Report

共 2 个 thread

---

### Thread 1: sea_to_user sefltest failure

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 11 Dec 2025 19:11:35 +0100 (CET)

#### 🤖 AI 总结

本邮件线程讨论了关于 `sea_to_user` 自测失败的问题，主要集中在如何解决测试中遇到的 EINJ 模块缺失的问题。

1. **原始问题**：Jiaqi Yan 在测试 `sea_to_user` 时，发现测试被跳过，错误信息显示无法找到 EINJ 模块，导致测试未能执行。具体表现为在尝试写入 EINJ 条目时出现“没有这样的文件或目录”的错误。

2. **之前讨论要点**：虽然没有明确的历史讨论记录，但参与者们认为测试失败与测试环境的配置有关，特别是与 EINJ 支持的相关性。Marc Zyngier 提到，Zenghui 的报告指出了潜在的逻辑缺陷，可能影响测试的有效性。

3. **本周的新讨论与进展**：本周的讨论中，Sebastian Ott 提出了检查测试机器是否支持 EINJ 的建议，包括检查固件日志、内核配置和模块加载情况。Jiaqi Yan 也表示将进一步完善测试代码，以提高测试的通用性和覆盖率。Marc Zyngier 计划与 Zhenghui 合作，改进测试，以便适应更广泛的环境。

总体而言，参与者们正在积极探讨如何解决测试失败的问题，并计划通过更好的环境适配和代码改进来提升测试的可靠性。

#### 📝 邮件列表

1. **[12-11 19:11]** Re: sea_to_user sefltest failure
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[12-11 18:19]** Re: sea_to_user sefltest failure
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[12-11 18:08]** Re: sea_to_user sefltest failure
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>
4. **[12-11 18:11]** Re: sea_to_user sefltest failure
   - 发件人: Jiaqi Yan <jiaqiyan@google.com>

---

### Thread 2: sea_to_user sefltest failure

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 11 Dec 2025 18:54:25 +0100 (CET)

#### 🤖 AI 总结

本邮件讨论的主题是关于 `sea_to_user` 自测失败的问题。Sebastian Ott 提出了一个具体的错误信息，指出在执行 `sea_to_user` 测试时，内存分配失败，导致 mmap() 调用返回错误。错误信息显示，系统无法分配内存，可能与其当前的配置有关。

在历史讨论中没有相关的背景信息，因此本周的新讨论是唯一的内容。Sebastian 提供了他当前的内核配置，指出了一些与大页内存（hugepage）相关的选项，并询问这些配置是否可能导致测试失败。他提到可能需要在代码中添加某种逻辑来跳过测试，但也质疑这样做是否值得，认为自己的配置可能过于特殊。

总的来说，本周的讨论集中在 `sea_to_user` 测试失败的具体原因及其与内核配置的关系上，Sebastian 正在寻求对该问题的进一步理解和建议。

#### 📝 邮件列表

1. **[12-11 18:54]** sea_to_user sefltest failure
   - 发件人: Sebastian Ott <sebott@redhat.com>

---

## 📌 Other

共 1 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v4 00/11] arm64: EL2 support

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Thu,  4 Dec 2025 14:23:27 +0000

#### 🤖 AI 总结

本邮件线程讨论了为 arm64 架构的 KVM 单元测试添加 EL2 支持的补丁（PATCH v4 00/11）。该补丁的主要内容是引入一个环境变量 EL2，允许用户在 QEMU/kvmtool 启动时选择在 EL2 级别运行。

在历史讨论中，Joey Gouly 提出了补丁的多个改动，包括修复了 checkpatch.pl 的问题、调整了 EL2 环境变量的命名，并解决了在二级核心上的 SCTLR_ELx 初始化问题。补丁得到了 Marc Zyngier 和 Eric Auger 的认可。

本周的新讨论中，Joey Gouly 针对 Andrew Jones 的反馈进行了修改，调整了 EL2 环境变量的条件判断，使其支持 "1"、"Y" 和 "y" 三种输入形式。此外，他还采用了其他邮件中建议的 test_exception_prep() 函数。Joey 表示将于下周发布下一个版本，尽管临近假期。整体来看，讨论进展顺利，补丁在逐步完善中。

#### 📝 邮件列表

1. **[12-04 14:23]** [kvm-unit-tests PATCH v4 00/11] arm64: EL2 support
   - 发件人: Joey Gouly <joey.gouly@arm.com>
2. **[12-04 14:23]** [kvm-unit-tests PATCH v4 11/11] arm64: add EL2 environment variable
   - 发件人: Joey Gouly <joey.gouly@arm.com>
3. **[12-04 11:17]** Re: [kvm-unit-tests PATCH v4 11/11] arm64: add EL2 environment
 variable
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
4. **[12-12 16:03]** Re: [kvm-unit-tests PATCH v4 11/11] arm64: add EL2 environment
 variable
   - 发件人: Joey Gouly <joey.gouly@arm.com>

---

