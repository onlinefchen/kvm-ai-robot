# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-27 11:01:02

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 301
- **总 Thread 数**: 26
- **大型 Thread** (>20封): 5 个

### 分类分布

- **PATCH**: 22 threads (294 邮件)
- **RFC**: 2 threads (3 邮件)
- **GIT PULL**: 1 threads (2 邮件)
- **Discussion**: 1 threads (2 邮件)

---

## 📌 PATCH

共 22 个 thread

---

### Thread 1: [PATCH v2 00/27] KVM: arm64: SCTLR2, DoubleFault2, and NV external abort fixes

**📧 邮件数**: 36 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 16 Jun 2025 16:02:41 -0700

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的多个补丁，主要集中在 SCTLR2、DoubleFault2 和 NV 外部中止的修复上。

1. **原始补丁内容**：该补丁系列（共27个补丁）旨在实现对 SCTLR2、DoubleFault2 和 NV 外部中止的支持，特别是针对 KVM 的异常处理和状态管理进行了改进。补丁中涉及的关键特性包括 FEAT_RAS、FEAT_SCTLR2 和 FEAT_DoubleFault2。

2. **之前讨论要点**：在历史讨论中，开发者们对补丁的设计和实现进行了初步审查，提出了对异常处理、状态管理和特性支持的建议。Marc Zyngier 提出了对某些补丁的具体改进意见，强调了在处理异常时需要考虑的细节。

3. **本周新讨论与进展**：本周的讨论集中在补丁的具体实现细节上，Oliver Upton 针对每个补丁进行了详细说明，并对如何处理 SErrors 和 SEA（Synchronous External Abort）的路由进行了深入探讨。Marc Zyngier 对补丁的整体方向表示认可，并提出了一些小的改进建议。最终，Upton 收到了 Zyngier 的审核通过，确认补丁在大多数方面是有效的。

总体而言，本周的讨论推动了对 KVM arm64 架构下异常处理的进一步完善，确保了对新特性的支持和现有功能的稳定性。

#### 📝 邮件列表

1. **[06-16 16:02]** [PATCH v2 00/27] KVM: arm64: SCTLR2, DoubleFault2, and NV external abort fixes
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[06-16 16:02]** [PATCH v2 01/27] arm64: Detect FEAT_SCTLR2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[06-16 16:02]** [PATCH v2 02/27] arm64: Detect FEAT_DoubleFault2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[06-16 16:02]** [PATCH v2 03/27] KVM: arm64: Add helper to identify a nested context
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[06-16 16:02]** [PATCH v2 04/27] KVM: arm64: Treat vCPU with pending SError as runnable
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
6. **[06-16 16:02]** [PATCH v2 05/27] KVM: arm64: nv: Respect exception routing rules for SEAs
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[06-16 16:02]** [PATCH v2 06/27] KVM: arm64: nv: Honor SError exception routing / masking
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[06-16 16:02]** [PATCH v2 07/27] KVM: arm64: nv: Add FEAT_RAS vSError sys regs to table
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[06-16 16:02]** [PATCH v2 08/27] KVM: arm64: nv: Use guest hypervisor's vSError state
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[06-16 16:02]** [PATCH v2 09/27] KVM: arm64: nv: Advertise support for FEAT_RAS
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[06-16 16:02]** [PATCH v2 10/27] KVM: arm64: nv: Describe trap behavior of SCTLR2_EL1
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
12. **[06-16 16:02]** [PATCH v2 11/27] KVM: arm64: Wire up SCTLR2_ELx sysreg descriptors
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[06-16 16:02]** [PATCH v2 12/27] KVM: arm64: Context switch SCTLR2_ELx when advertised to the guest
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
14. **[06-16 16:02]** [PATCH v2 13/27] KVM: arm64: Enable SCTLR2 when advertised to the guest
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
15. **[06-16 16:02]** [PATCH v2 14/27] KVM: arm64: Describe SCTLR2_ELx RESx masks
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
16. **[06-16 16:02]** [PATCH v2 15/27] KVM: arm64: Factor out helper for selecting exception target EL
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
17. **[06-16 16:02]** [PATCH v2 16/27] KVM: arm64: nv: Ensure Address size faults affect correct ESR
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
18. **[06-16 16:02]** [PATCH v2 17/27] KVM: arm64: Route SEAs to the SError vector when EASE is set
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
19. **[06-16 16:02]** [PATCH v2 18/27] KVM: arm64: nv: Handle effects of HCRX_EL2.TMEA on SError injection
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
20. **[06-16 16:03]** [PATCH v2 19/27] KVM: arm64: Take "masked" SEAs to EL2 when TMEA is set
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
21. **[06-16 16:03]** [PATCH v2 20/27] KVM: arm64: nv: Enable vSErrors when HCRX_EL2.TMEA is set
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
22. **[06-16 16:03]** [PATCH v2 21/27] KVM: arm64: Advertise support for FEAT_SCTLR2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
23. **[06-16 16:03]** [PATCH v2 22/27] KVM: arm64: Advertise support for FEAT_DoubleFault2
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
24. **[06-16 16:03]** [PATCH v2 23/27] KVM: arm64: Don't retire MMIO instruction w/ pending (emulated) SError
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
25. **[06-16 16:03]** [PATCH v2 24/27] KVM: arm64: selftests: Add basic SError injection test
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
26. **[06-16 16:03]** [PATCH v2 25/27] KVM: arm64: selftests: Test SEAs are taken to SError vector when EASE=1
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
27. **[06-16 16:03]** [PATCH v2 26/27] KVM: arm64: selftests: Add SCTLR2_EL1 to get-reg-list
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
28. **[06-16 16:03]** [PATCH v2 27/27] KVM: arm64: selftests: Catch up set_id_regs with the kernel
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
29. **[06-21 10:51]** Re: [PATCH v2 05/27] KVM: arm64: nv: Respect exception routing rules for SEAs
   - 发件人: Marc Zyngier <maz@kernel.org>
30. **[06-21 11:47]** Re: [PATCH v2 06/27] KVM: arm64: nv: Honor SError exception routing / masking
   - 发件人: Marc Zyngier <maz@kernel.org>
31. **[06-21 12:09]** Re: [PATCH v2 08/27] KVM: arm64: nv: Use guest hypervisor's vSError state
   - 发件人: Marc Zyngier <maz@kernel.org>
32. **[06-21 12:34]** Re: [PATCH v2 14/27] KVM: arm64: Describe SCTLR2_ELx RESx masks
   - 发件人: Marc Zyngier <maz@kernel.org>
33. **[06-21 12:54]** Re: [PATCH v2 17/27] KVM: arm64: Route SEAs to the SError vector when EASE is set
   - 发件人: Marc Zyngier <maz@kernel.org>
34. **[06-21 14:03]** Re: [PATCH v2 18/27] KVM: arm64: nv: Handle effects of HCRX_EL2.TMEA on SError injection
   - 发件人: Marc Zyngier <maz@kernel.org>
35. **[06-22 09:39]** Re: [PATCH v2 19/27] KVM: arm64: Take "masked" SEAs to EL2 when TMEA is set
   - 发件人: Marc Zyngier <maz@kernel.org>
36. **[06-22 10:25]** Re: [PATCH v2 00/27] KVM: arm64: SCTLR2, DoubleFault2, and NV external abort fixes
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [PATCH v3 00/62] KVM: iommu: Overhaul device posted IRQs support

**📧 邮件数**: 33 | **👥 参与者**: 5 | **📅 开始时间**: Wed, 11 Jun 2025 15:45:03 -0700

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（内核虚拟机）的多个补丁，主要集中在对设备中断（IRQ）的支持进行大规模重构。补丁系列的核心是改进 ARM64 架构下的设备中断处理，特别是与 IOMMU（输入输出内存管理单元）相关的部分。

**历史讨论**中，补丁的第一部分涉及对 ARM64 的修复，确保在更新 IRQ 路由时能够正确处理类型变化，并在解除 vLPI（虚拟本地中断）映射失败时发出警告。参与者讨论了这些补丁的必要性及其对现有代码的影响，尤其是如何避免在中断路由更新时出现错误。

**本周新讨论**中，参与者对多个补丁进行了细致的审查和反馈。Naveen N Rao 提出了对某些补丁代码可读性的建议，并对如何处理 APIC（高级可编程中断控制器）虚拟化的复杂性进行了讨论。此外，Sean Christopherson 也回应了关于补丁的实现细节，强调了在特定情况下对 APIC 状态的管理需要谨慎处理。最终，部分补丁获得了参与者的认可，并计划在接下来的版本中合并。

总体来看，本周的讨论集中在补丁的细节优化和潜在问题的解决上，显示出参与者对 KVM 设备中断处理的持续关注和改进的努力。

#### 📝 邮件列表

1. **[06-11 15:45]** [PATCH v3 00/62] KVM: iommu: Overhaul device posted IRQs support
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[06-11 15:45]** [PATCH v3 01/62] KVM: arm64: Explicitly treat routing entry type
 changes as changes
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[06-11 15:45]** [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[06-11 15:45]** [PATCH v3 12/62] KVM: SVM: Inhibit AVIC if ID is too big instead of
 rejecting vCPU creation
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[06-11 15:45]** [PATCH v3 13/62] KVM: SVM: Drop redundant check in AVIC code on ID
 during vCPU creation
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[06-11 15:45]** [PATCH v3 14/62] KVM: SVM: Track AVIC tables as natively sized
 pointers, not "struct pages"
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[06-11 15:45]** [PATCH v3 15/62] KVM: SVM: Drop superfluous "cache" of AVIC Physical
 ID entry pointer
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[06-11 15:45]** [PATCH v3 17/62] KVM: SVM: Add enable_ipiv param, never set IsRunning
 if disabled
   - 发件人: Sean Christopherson <seanjc@google.com>
9. **[06-11 15:45]** [PATCH v3 38/62] KVM: SVM: Take and hold ir_list_lock across IRTE
 updates in IOMMU
   - 发件人: Sean Christopherson <seanjc@google.com>
10. **[06-12 12:59]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[06-12 07:34]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Sean Christopherson <seanjc@google.com>
12. **[06-13 13:47]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
13. **[06-17 19:55]** Re: [PATCH v3 12/62] KVM: SVM: Inhibit AVIC if ID is too big instead
 of rejecting vCPU creation
   - 发件人: Naveen N Rao <naveen@kernel.org>
14. **[06-17 20:19]** Re: [PATCH v3 13/62] KVM: SVM: Drop redundant check in AVIC code on
 ID during vCPU creation
   - 发件人: Naveen N Rao <naveen@kernel.org>
15. **[06-17 20:31]** Re: [PATCH v3 14/62] KVM: SVM: Track AVIC tables as natively sized
 pointers, not "struct pages"
   - 发件人: Naveen N Rao <naveen@kernel.org>
16. **[06-17 21:12]** Re: [PATCH v3 38/62] KVM: SVM: Take and hold ir_list_lock across
 IRTE updates in IOMMU
   - 发件人: Naveen N Rao <naveen@kernel.org>
17. **[06-17 09:10]** Re: [PATCH v3 12/62] KVM: SVM: Inhibit AVIC if ID is too big instead
 of rejecting vCPU creation
   - 发件人: Sean Christopherson <seanjc@google.com>
18. **[06-17 09:33]** Re: [PATCH v3 13/62] KVM: SVM: Drop redundant check in AVIC code on
 ID during vCPU creation
   - 发件人: Sean Christopherson <seanjc@google.com>
19. **[06-18 20:03]** Re: [PATCH v3 12/62] KVM: SVM: Inhibit AVIC if ID is too big instead
 of rejecting vCPU creation
   - 发件人: Naveen N Rao <naveen.rao@amd.com>
20. **[06-18 20:09]** Re: [PATCH v3 13/62] KVM: SVM: Drop redundant check in AVIC code on
 ID during vCPU creation
   - 发件人: Naveen N Rao <naveen.rao@amd.com>
21. **[06-18 13:59]** Re: [PATCH v3 12/62] KVM: SVM: Inhibit AVIC if ID is too big instead
 of rejecting vCPU creation
   - 发件人: Sean Christopherson <seanjc@google.com>
22. **[06-19 16:39]** Re: [PATCH v3 15/62] KVM: SVM: Drop superfluous "cache" of AVIC
 Physical ID entry pointer
   - 发件人: Naveen N Rao <naveen@kernel.org>
23. **[06-19 17:01]** Re: [PATCH v3 17/62] KVM: SVM: Add enable_ipiv param, never set
 IsRunning if disabled
   - 发件人: Naveen N Rao <naveen@kernel.org>
24. **[06-19 17:31]** Re: [PATCH v3 17/62] KVM: SVM: Add enable_ipiv param, never set
 IsRunning if disabled
   - 发件人: Naveen N Rao <naveen@kernel.org>
25. **[06-19 13:36]** Re: (subset) [PATCH v3 01/62] KVM: arm64: Explicitly treat routing entry type changes as changes
   - 发件人: Marc Zyngier <maz@kernel.org>
26. **[06-20 07:39]** Re: [PATCH v3 17/62] KVM: SVM: Add enable_ipiv param, never set
 IsRunning if disabled
   - 发件人: Sean Christopherson <seanjc@google.com>
27. **[06-20 10:22]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Sean Christopherson <seanjc@google.com>
28. **[06-20 19:00]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: David Woodhouse <dwmw2@infradead.org>
29. **[06-20 11:48]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
30. **[06-20 12:04]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Sean Christopherson <seanjc@google.com>
31. **[06-20 12:27]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
32. **[06-20 13:31]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Sean Christopherson <seanjc@google.com>
33. **[06-20 13:45]** Re: [PATCH v3 02/62] KVM: arm64: WARN if unmapping vLPI fails
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 3: [PATCH v2 00/23] ARM64 PMU Partitioning

**📧 邮件数**: 31 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 20 Jun 2025 22:13:00 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的 PMU（性能监控单元）分区的补丁系列，主要包括以下内容：

1. **原始补丁/问题内容**：
   - 提出的补丁系列旨在创建一种新的 PMU 分区方案，使得可以为虚拟机（VM）保留一部分计数器，从而减少性能开销。补丁中引入了新的命令行参数和 ioctl 接口，以支持在运行时配置 PMU 的分区。

2. **之前讨论要点**：
   - 之前的讨论集中在如何有效地实现 PMU 的分区，确保在虚拟机中能够直接访问这些计数器。参与者提出了对命令行参数的修改建议，以便更好地表达分区配置的意图。此外，讨论中提到需要处理不同硬件特性对 PMU 分区的影响。

3. **本周的新讨论、进展或结论**：
   - 本周的讨论主要集中在补丁的具体实现细节上，包括如何在 KVM 中设置和管理 PMU 的分区。补丁中添加了对 PMU 事件过滤的支持，确保在加载虚拟机时重新检查事件过滤器。此外，补丁还引入了新的 ioctl 接口，以便在虚拟 CPU 上启用 PMU 分区。参与者对补丁的实现提出了反馈，建议进一步简化参数设置，并确保与现有的 KVM 功能兼容。

总的来说，本线程的讨论围绕 ARM64 PMU 分区的实现进行了深入的技术探讨，涉及补丁的设计、实现细节及其与 KVM 的集成。

#### 📝 邮件列表

1. **[06-20 22:13]** [PATCH v2 00/23] ARM64 PMU Partitioning
   - 发件人: Colton Lewis <coltonlewis@google.com>
2. **[06-20 22:13]** [PATCH v2 01/23] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Colton Lewis <coltonlewis@google.com>
3. **[06-20 22:13]** [PATCH v2 02/23] arm64: Generate sign macro for sysreg Enums
   - 发件人: Colton Lewis <coltonlewis@google.com>
4. **[06-20 22:13]** [PATCH v2 03/23] arm64: cpufeature: Add cpucap for PMICNTR
   - 发件人: Colton Lewis <coltonlewis@google.com>
5. **[06-20 22:13]** [PATCH v2 04/23] arm64: Define PMI{CNTR,FILTR}_EL0 as undef_access
   - 发件人: Colton Lewis <coltonlewis@google.com>
6. **[06-20 22:13]** [PATCH v2 05/23] KVM: arm64: Cleanup PMU includes
   - 发件人: Colton Lewis <coltonlewis@google.com>
7. **[06-20 22:13]** [PATCH v2 06/23] KVM: arm64: Reorganize PMU functions
   - 发件人: Colton Lewis <coltonlewis@google.com>
8. **[06-20 22:13]** [PATCH v2 07/23] perf: arm_pmuv3: Introduce method to partition the PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
9. **[06-20 22:13]** [PATCH v2 07/23] perf: pmuv3: Introduce method to partition the PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
10. **[06-20 22:13]** [PATCH v2 08/23] perf: arm_pmuv3: Generalize counter bitmasks
   - 发件人: Colton Lewis <coltonlewis@google.com>
11. **[06-20 22:13]** [PATCH v2 09/23] perf: arm_pmuv3: Keep out of guest counter partition
   - 发件人: Colton Lewis <coltonlewis@google.com>
12. **[06-20 22:13]** [PATCH v2 10/23] KVM: arm64: Correct kvm_arm_pmu_get_max_counters()
   - 发件人: Colton Lewis <coltonlewis@google.com>
13. **[06-20 22:13]** [PATCH v2 11/23] KVM: arm64: Set up FGT for Partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
14. **[06-20 22:13]** [PATCH v2 12/23] KVM: arm64: Writethrough trapped PMEVTYPER register
   - 发件人: Colton Lewis <coltonlewis@google.com>
15. **[06-20 22:13]** [PATCH v2 13/23] KVM: arm64: Use physical PMSELR for PMXEVTYPER if partitioned
   - 发件人: Colton Lewis <coltonlewis@google.com>
16. **[06-20 22:13]** [PATCH v2 14/23] KVM: arm64: Writethrough trapped PMOVS register
   - 发件人: Colton Lewis <coltonlewis@google.com>
17. **[06-20 22:13]** [PATCH v2 15/23] KVM: arm64: Write fast path PMU register handlers
   - 发件人: Colton Lewis <coltonlewis@google.com>
18. **[06-20 22:13]** [PATCH v2 16/23] KVM: arm64: Setup MDCR_EL2 to handle a partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
19. **[06-20 22:13]** [PATCH v2 17/23] KVM: arm64: Account for partitioning in PMCR_EL0 access
   - 发件人: Colton Lewis <coltonlewis@google.com>
20. **[06-20 22:13]** [PATCH v2 18/23] KVM: arm64: Context swap Partitioned PMU guest registers
   - 发件人: Colton Lewis <coltonlewis@google.com>
21. **[06-20 22:13]** [PATCH v2 19/23] KVM: arm64: Enforce PMU event filter at vcpu_load()
   - 发件人: Colton Lewis <coltonlewis@google.com>
22. **[06-20 22:13]** [PATCH v2 20/23] perf: arm_pmuv3: Handle IRQs for Partitioned PMU
 guest counters
   - 发件人: Colton Lewis <coltonlewis@google.com>
23. **[06-20 22:13]** [PATCH v2 20/23] perf: pmuv3: Handle IRQs for Partitioned PMU guest counters
   - 发件人: Colton Lewis <coltonlewis@google.com>
24. **[06-20 22:13]** [PATCH v2 21/23] KVM: arm64: Inject recorded guest interrupts
   - 发件人: Colton Lewis <coltonlewis@google.com>
25. **[06-20 22:13]** [PATCH v2 22/23] KVM: arm64: Add ioctl to partition the PMU when supported
   - 发件人: Colton Lewis <coltonlewis@google.com>
26. **[06-20 22:13]** [PATCH v2 23/23] KVM: arm64: selftests: Add test case for partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
27. **[06-20 17:44]** Re: [PATCH v2 01/23] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
28. **[06-20 17:45]** Re: [PATCH v2 03/23] arm64: cpufeature: Add cpucap for PMICNTR
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
29. **[06-20 18:06]** Re: [PATCH v2 07/23] perf: arm_pmuv3: Introduce method to partition
 the PMU
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
30. **[06-21 22:56]** Re: [PATCH v2 05/23] KVM: arm64: Cleanup PMU includes
   - 发件人: kernel test robot <lkp@intel.com>
31. **[06-22 17:32]** Re: [PATCH v2 17/23] KVM: arm64: Account for partitioning in
 PMCR_EL0 access
   - 发件人: kernel test robot <lkp@intel.com>

---

### Thread 4: [PATCH v3 00/15] KVM: Introduce KVM Userfault

**📧 邮件数**: 29 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 18 Jun 2025 04:24:09 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个名为“KVM Userfault”的补丁系列，旨在为KVM（Kernel-based Virtual Machine）引入用户故障处理机制。该补丁的主要内容包括引入一个新的内存槽标志KVM_MEM_USERFAULT，以及相关的用户空间位图，用于控制哪些页面的访问会导致KVM退出到用户空间。

在历史讨论中，补丁的背景主要集中在KVM缺乏对后复制实时迁移的支持，以及现有的基于userfaultfd的后复制机制在扩展性方面的不足。KVM Userfault的实现可以显著改善这些问题，特别是在处理大量虚拟CPU时。

本周的新讨论中，开发者James Houghton提交了补丁的第三版（v3），并感谢Sean等人的反馈。他提到，v3版本中整合了之前的建议，修复了一些问题，并增加了对KVM Userfault的支持。讨论中还提到，该补丁可能与Fuad的用户映射支持存在冲突，特别是在arm64架构下。邮件中还涉及了对KVM Userfault的文档更新、测试用例的添加以及与现有功能的兼容性问题。

总的来说，本周的讨论集中在补丁的细节修正、架构兼容性以及如何优化用户故障处理流程上，开发者们积极交流了实现中的挑战和解决方案。

#### 📝 邮件列表

1. **[06-18 04:24]** [PATCH v3 00/15] KVM: Introduce KVM Userfault
   - 发件人: James Houghton <jthoughton@google.com>
2. **[06-18 04:24]** [PATCH v3 01/15] KVM: x86/mmu: Move "struct kvm_page_fault"
 definition to asm/kvm_host.h
   - 发件人: James Houghton <jthoughton@google.com>
3. **[06-18 04:24]** [PATCH v3 02/15] KVM: arm64: Add "struct kvm_page_fault" to gather
 common fault variables
   - 发件人: James Houghton <jthoughton@google.com>
4. **[06-18 04:24]** [PATCH v3 03/15] KVM: arm64: x86: Require "struct kvm_page_fault" for
 memory fault exits
   - 发件人: James Houghton <jthoughton@google.com>
5. **[06-18 04:24]** [PATCH v3 04/15] KVM: Add common infrastructure for KVM Userfaults
   - 发件人: James Houghton <jthoughton@google.com>
6. **[06-18 04:24]** [PATCH v3 05/15] KVM: x86: Add support for KVM userfault exits
   - 发件人: James Houghton <jthoughton@google.com>
7. **[06-18 04:24]** [PATCH v3 06/15] KVM: arm64: Add support for KVM userfault exits
   - 发件人: James Houghton <jthoughton@google.com>
8. **[06-18 04:24]** [PATCH v3 07/15] KVM: Enable and advertise support for KVM userfault exits
   - 发件人: James Houghton <jthoughton@google.com>
9. **[06-18 04:24]** [PATCH v3 08/15] KVM: selftests: Fix vm_mem_region_set_flags docstring
   - 发件人: James Houghton <jthoughton@google.com>
10. **[06-18 04:24]** [PATCH v3 09/15] KVM: selftests: Fix prefault_mem logic
   - 发件人: James Houghton <jthoughton@google.com>
11. **[06-18 04:24]** [PATCH v3 10/15] KVM: selftests: Add va_start/end into uffd_desc
   - 发件人: James Houghton <jthoughton@google.com>
12. **[06-18 04:24]** [PATCH v3 11/15] KVM: selftests: Add KVM Userfault mode to demand_paging_test
   - 发件人: James Houghton <jthoughton@google.com>
13. **[06-18 04:24]** [PATCH v3 12/15] KVM: selftests: Inform set_memory_region_test of KVM_MEM_USERFAULT
   - 发件人: James Houghton <jthoughton@google.com>
14. **[06-18 04:24]** [PATCH v3 13/15] KVM: selftests: Add KVM_MEM_USERFAULT + guest_memfd
 toggle tests
   - 发件人: James Houghton <jthoughton@google.com>
15. **[06-18 04:24]** [PATCH v3 14/15] KVM: Documentation: Fix section number for KVM_CAP_ARM_WRITABLE_IMP_ID_REGS
   - 发件人: James Houghton <jthoughton@google.com>
16. **[06-18 04:24]** [PATCH v3 15/15] KVM: Documentation: Add KVM_CAP_USERFAULT and
 KVM_MEM_USERFAULT details
   - 发件人: James Houghton <jthoughton@google.com>
17. **[06-18 12:26]** Re: [PATCH v3 02/15] KVM: arm64: Add "struct kvm_page_fault" to
 gather common fault variables
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
18. **[06-18 12:40]** Re: [PATCH v3 04/15] KVM: Add common infrastructure for KVM
 Userfaults
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
19. **[06-18 13:00]** Re: [PATCH v3 03/15] KVM: arm64: x86: Require "struct
 kvm_page_fault" for memory fault exits
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
20. **[06-18 13:33]** Re: [PATCH v3 04/15] KVM: Add common infrastructure for KVM Userfaults
   - 发件人: Sean Christopherson <seanjc@google.com>
21. **[06-18 13:38]** Re: [PATCH v3 04/15] KVM: Add common infrastructure for KVM Userfaults
   - 发件人: James Houghton <jthoughton@google.com>
22. **[06-18 13:41]** Re: [PATCH v3 04/15] KVM: Add common infrastructure for KVM Userfaults
   - 发件人: James Houghton <jthoughton@google.com>
23. **[06-18 13:47]** Re: [PATCH v3 03/15] KVM: arm64: x86: Require "struct kvm_page_fault"
 for memory fault exits
   - 发件人: Sean Christopherson <seanjc@google.com>
24. **[06-18 14:17]** Re: [PATCH v3 02/15] KVM: arm64: Add "struct kvm_page_fault" to
 gather common fault variables
   - 发件人: Sean Christopherson <seanjc@google.com>
25. **[06-18 15:43]** Re: [PATCH v3 04/15] KVM: Add common infrastructure for KVM
 Userfaults
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
26. **[06-18 16:14]** Re: [PATCH v3 03/15] KVM: arm64: x86: Require "struct
 kvm_page_fault" for memory fault exits
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
27. **[06-18 16:24]** Re: [PATCH v3 00/15] KVM: Introduce KVM Userfault
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
28. **[06-18 18:22]** Re: [PATCH v3 03/15] KVM: arm64: x86: Require "struct kvm_page_fault"
 for memory fault exits
   - 发件人: Sean Christopherson <seanjc@google.com>
29. **[06-18 18:27]** Re: [PATCH v3 04/15] KVM: Add common infrastructure for KVM Userfaults
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 5: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the host
 for software protected VMs

**📧 邮件数**: 28 | **👥 参与者**: 5 | **📅 开始时间**: Wed, 11 Jun 2025 14:33:12 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM 的补丁系列，主要目的是在主机上映射由 guest_memfd 支持的内存，以增强软件保护虚拟机的安全性。补丁的关键内容包括支持在主机用户空间中映射 guest_memfd 页面，这对于像 Firecracker 这样的虚拟机监控器（VMM）非常重要。

在历史讨论中，参与者们对补丁进行了多次反馈，主要集中在补丁的命名和功能描述上。Fuad Tabba 提出了一系列补丁，旨在解决之前版本中的反馈，并重新基于 Linux 6.16-rc1。Sean Christopherson 对补丁的描述提出了质疑，认为 changelog 中缺乏足够的上下文和用例说明，导致理解困难。

在本周的新讨论中，参与者们继续围绕补丁的命名和功能进行深入探讨。Fuad 表示将根据反馈修改补丁描述，确保术语清晰。David Hildenbrand 和其他参与者提出了对“共享”和“私有”内存的定义问题，讨论了如何更好地描述 guest_memfd 的内存特性，以避免混淆。最终，大家达成共识，认为需要清晰地定义补丁中涉及的内存类型，并在后续版本中改进文档和 changelog。

总体来看，本周的讨论强调了补丁的命名、功能描述以及文档的重要性，参与者们希望通过更清晰的表达来促进理解和后续开发。

#### 📝 邮件列表

1. **[06-11 14:33]** [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the host
 for software protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[06-11 14:33]** [PATCH v12 04/18] KVM: x86: Rename kvm->arch.has_private_mem to kvm->arch.supports_gmem
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[06-11 14:33]** [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[06-13 13:35]** Re: [PATCH v12 04/18] KVM: x86: Rename kvm->arch.has_private_mem to kvm->arch.supports_gmem
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[06-13 14:03]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[06-16 07:52]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[06-16 08:13]** Re: [PATCH v12 04/18] KVM: x86: Rename kvm->arch.has_private_mem to kvm->arch.supports_gmem
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[06-16 08:44]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map
 guest_memfd pages
   - 发件人: Ira Weiny <ira.weiny@intel.com>
9. **[06-16 16:03]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: David Hildenbrand <david@redhat.com>
10. **[06-16 15:16]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Fuad Tabba <tabba@google.com>
11. **[06-16 16:16]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: David Hildenbrand <david@redhat.com>
12. **[06-16 16:20]** Re: [PATCH v12 04/18] KVM: x86: Rename kvm->arch.has_private_mem to
 kvm->arch.supports_gmem
   - 发件人: David Hildenbrand <david@redhat.com>
13. **[06-16 16:25]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: David Hildenbrand <david@redhat.com>
14. **[06-17 16:04]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Sean Christopherson <seanjc@google.com>
15. **[06-17 17:40]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Sean Christopherson <seanjc@google.com>
16. **[06-18 10:15]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: David Hildenbrand <david@redhat.com>
17. **[06-18 17:20]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
18. **[06-18 11:25]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: David Hildenbrand <david@redhat.com>
19. **[06-18 11:27]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: David Hildenbrand <david@redhat.com>
20. **[06-18 17:44]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
21. **[06-18 11:59]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: David Hildenbrand <david@redhat.com>
22. **[06-18 18:42]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
23. **[06-18 13:14]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: David Hildenbrand <david@redhat.com>
24. **[06-18 12:18]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Fuad Tabba <tabba@google.com>
25. **[06-18 20:17]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
26. **[06-18 15:16]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd
 pages
   - 发件人: David Hildenbrand <david@redhat.com>
27. **[06-18 18:48]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Sean Christopherson <seanjc@google.com>
28. **[06-18 18:50]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 6: [PATCH v7 0/5] KVM: arm64: Map GPU device memory as cacheable

**📧 邮件数**: 18 | **👥 参与者**: 5 | **📅 开始时间**: Wed, 18 Jun 2025 06:55:36 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（内核虚拟机）在 arm64 架构下如何将 GPU 设备内存映射为可缓存的内存。原始的 patch 提出了将 GPU 设备内存映射为可缓存的需求，尤其是在 Grace Hopper/Blackwell 超级芯片等平台上，这些平台的 CPU 可访问缓存一致的 GPU 内存。

在历史讨论中，参与者们探讨了 KVM 目前的内存映射限制，指出 KVM 只能将内存区域标记为 NORMAL 或 DEVICE_nGnRE，这限制了未添加到内核的设备内存的可缓存性。为了解决这个问题，patch 提出了通过 VMA（虚拟内存区域）标志来实现可缓存的映射。

本周的新讨论中，Ankit Agrawal 提交了五个补丁，逐步完善了这一功能。补丁的主要进展包括：
1. 引入了新的函数来检查硬件是否支持缓存管理。
2. 阻止用户空间将可缓存的 PFNMAP 映射为非缓存，以避免安全风险。
3. 允许根据 VMA 标志进行缓存的二级映射。
4. 引入了新的 KVM 能力，允许用户空间查询是否支持可缓存的 PFNMAP。

参与者们对补丁进行了审查和讨论，提出了一些改进建议，确保代码的清晰性和安全性。整体来看，这些补丁为 KVM 提供了更灵活的内存管理能力，特别是在处理 GPU 设备内存时。

#### 📝 邮件列表

1. **[06-18 06:55]** [PATCH v7 0/5] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: ankita <ankita@nvidia.com>
2. **[06-18 06:55]** [PATCH v7 1/5] KVM: arm64: Rename symbols to reflect whether CMO may be used
   - 发件人: ankita <ankita@nvidia.com>
3. **[06-18 06:55]** [PATCH v7 2/5] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: ankita <ankita@nvidia.com>
4. **[06-18 06:55]** [PATCH v7 3/5] KVM: arm64: New function to determine hardware cache management support
   - 发件人: ankita <ankita@nvidia.com>
5. **[06-18 06:55]** [PATCH v7 4/5] KVM: arm64: Allow cacheable stage 2 mapping using VMA flags
   - 发件人: ankita <ankita@nvidia.com>
6. **[06-18 06:55]** [PATCH v7 5/5] KVM: arm64: Expose new KVM cap for cacheable PFNMAP
   - 发件人: ankita <ankita@nvidia.com>
7. **[06-18 15:28]** Re: [PATCH v7 1/5] KVM: arm64: Rename symbols to reflect whether CMO
 may be used
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
8. **[06-18 15:35]** Re: [PATCH v7 1/5] KVM: arm64: Rename symbols to reflect whether CMO
 may be used
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
9. **[06-18 16:46]** Re: [PATCH v7 2/5] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
10. **[06-18 17:12]** Re: [PATCH v7 3/5] KVM: arm64: New function to determine hardware
 cache management support
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
11. **[06-18 17:34]** Re: [PATCH v7 4/5] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Catalin Marinas <catalin.marinas@arm.com>
12. **[06-18 13:38]** Re: [PATCH v7 4/5] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
13. **[06-19 02:21]** Re: [PATCH v7 2/5] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
14. **[06-19 02:22]** Re: [PATCH v7 1/5] KVM: arm64: Rename symbols to reflect whether CMO
 may be used
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
15. **[06-19 12:14]** Re: [PATCH v7 4/5] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
16. **[06-19 11:16]** Re: [PATCH v7 4/5] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
17. **[06-19 12:03]** Re: [PATCH v7 4/5] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Donald Dutile <ddutile@redhat.com>
18. **[06-19 16:46]** Re: [PATCH v7 4/5] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Ankit Agrawal <ankita@nvidia.com>

---

### Thread 7: [PATCH v8 00/14] arm: rework id register storage

**📧 邮件数**: 16 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 17 Jun 2025 17:39:17 +0200

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM 架构的 ID 寄存器存储重构的补丁系列（[PATCH v8 00/14]）。该补丁旨在改进 ID 寄存器的存储方式，使其更为高效和一致。

**原始补丁/问题内容**：
补丁系列的核心是重新设计 ARM 处理器的 ID 寄存器存储方式，具体包括将寄存器定义从结构体字段转移到数组中，以便更灵活地管理和访问。

**之前讨论要点**：
在之前的讨论中，开发者 Cornelia Huck 针对不同版本的补丁（v1 到 v7）进行了多次迭代，主要集中在修复反馈、增强脚本的健壮性、更新维护者信息等方面。补丁的目标是简化寄存器的生成过程，并确保生成的代码与 Linux 内核的 sysreg 文件保持一致。

**本周的新讨论、进展或结论**：
本周的讨论中，补丁 v8 版本被提交，主要包括：
1. 引入了用于自动生成系统寄存器定义的脚本，简化了寄存器定义的维护。
2. 修复了之前版本中的一些问题，并确保与当前 Linux 内核的 sysreg 结构兼容。
3. 讨论了如何使用生成的脚本更新寄存器定义文件，确保 QEMU 的 ARM 模型能够正确反映最新的 ARM 架构特性。

此外，补丁还包括对 KVM 代码的清理，使用了更简洁的文件描述符（fd）替代了之前的 fdarray 数组，提升了代码的可读性和维护性。

#### 📝 邮件列表

1. **[06-17 17:39]** [PATCH v8 00/14] arm: rework id register storage
   - 发件人: Cornelia Huck <cohuck@redhat.com>
2. **[06-17 17:39]** [PATCH v8 01/14] arm/cpu: Add sysreg definitions in cpu-sysregs.h
   - 发件人: Cornelia Huck <cohuck@redhat.com>
3. **[06-17 17:39]** [PATCH v8 02/14] arm/cpu: Store aa64isar0/aa64zfr0 into the idregs arrays
   - 发件人: Cornelia Huck <cohuck@redhat.com>
4. **[06-17 17:39]** [PATCH v8 03/14] arm/cpu: Store aa64isar1/2 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
5. **[06-17 17:39]** [PATCH v8 04/14] arm/cpu: Store aa64pfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
6. **[06-17 17:39]** [PATCH v8 05/14] arm/cpu: Store aa64mmfr0-3 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
7. **[06-17 17:39]** [PATCH v8 06/14] arm/cpu: Store aa64dfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
8. **[06-17 17:39]** [PATCH v8 07/14] arm/cpu: Store aa64smfr0 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
9. **[06-17 17:39]** [PATCH v8 08/14] arm/cpu: Store id_isar0-7 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
10. **[06-17 17:39]** [PATCH v8 09/14] arm/cpu: Store id_pfr0/1/2 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
11. **[06-17 17:39]** [PATCH v8 10/14] arm/cpu: Store id_dfr0/1 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
12. **[06-17 17:39]** [PATCH v8 11/14] arm/cpu: Store id_mmfr0-5 into the idregs array
   - 发件人: Cornelia Huck <cohuck@redhat.com>
13. **[06-17 17:39]** [PATCH v8 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Cornelia Huck <cohuck@redhat.com>
14. **[06-17 17:39]** [PATCH v8 13/14] arm/cpu: switch to a generated cpu-sysregs.h.inc
   - 发件人: Cornelia Huck <cohuck@redhat.com>
15. **[06-17 17:39]** [PATCH v8 14/14] arm/kvm: use fd instead of fdarray[2]
   - 发件人: Cornelia Huck <cohuck@redhat.com>
16. **[06-17 17:45]** Re: [PATCH v8 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 8: [PATCH v4 0/5] Add FIELD_MODIFY() helper

**📧 邮件数**: 13 | **👥 参与者**: 4 | **📅 开始时间**: Thu, 12 Jun 2025 21:46:07 +0800

#### 🤖 AI 总结

本邮件线程讨论的主题是增加一个名为 `FIELD_MODIFY()` 的辅助宏，以改进 Linux 内核中位域的处理。历史讨论中，Luo Jie 提出了该补丁系列，旨在通过 `FIELD_MODIFY()` 提供更严格的参数类型检查，替代现有的 `xxx_replace_bits()` 函数，并且计划将内核中已有的四个实例转换为使用新宏。Marc Zyngier 对此表示反对，认为现有的辅助函数已经足够，并不需要重复实现相同功能。

在本周的新讨论中，Luo Jie 决定在下一个版本中删除 ARM64 相关的补丁，仅保留 Coccinelle 脚本补丁。Markus Elfring 和 Will Deacon 提出了一些建议，认为需要更清晰地阐述 `FIELD_MODIFY()` 的优势，以及其相较于现有功能的价值。Will 指出，之前的讨论中并未明确说明新宏的必要性，建议从这一点入手进行解释。最终，Luo Jie 表示，经过讨论，发现 ARM64 中的现有代码已经能够支持严格的参数检查，因此在特定情况下使用 `FIELD_MODIFY()` 并没有明显的优势。

#### 📝 邮件列表

1. **[06-12 21:46]** [PATCH v4 0/5] Add FIELD_MODIFY() helper
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
2. **[06-12 21:46]** [PATCH v4 1/5] coccinelle: misc: Add field_modify script
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
3. **[06-12 21:46]** [PATCH v4 2/5] arm64: tlb: Convert the opencoded field modify
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
4. **[06-12 15:11]** Re: [PATCH v4 0/5] Add FIELD_MODIFY() helper
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[06-12 18:48]** Re: [cocci] [PATCH v4 1/5] coccinelle: misc: Add field_modify script
   - 发件人: Markus Elfring <Markus.Elfring@web.de>
6. **[06-12 22:15]** Re: [cocci] [PATCH v4 2/5] arm64: tlb: Convert the opencoded field
 modify
   - 发件人: Markus Elfring <Markus.Elfring@web.de>
7. **[06-16 18:06]** Re: [PATCH v4 0/5] Add FIELD_MODIFY() helper
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
8. **[06-16 18:28]** Re: [cocci] [PATCH v4 1/5] coccinelle: misc: Add field_modify script
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
9. **[06-16 18:37]** Re: [cocci] [PATCH v4 2/5] arm64: tlb: Convert the opencoded field
 modify
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
10. **[06-16 11:41]** Re: [cocci] [PATCH v4 2/5] arm64: tlb: Convert the opencoded field
 modify
   - 发件人: Will Deacon <will@kernel.org>
11. **[06-16 15:52]** Re: [cocci] [v4 2/5] arm64: tlb: Convert the opencoded field modify
   - 发件人: Markus Elfring <Markus.Elfring@web.de>
12. **[06-17 00:19]** Re: [cocci] [PATCH v4 2/5] arm64: tlb: Convert the opencoded field
 modify
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
13. **[06-17 00:19]** Re: [cocci] [v4 2/5] arm64: tlb: Convert the opencoded field modify
   - 发件人: Luo Jie <quic_luoj@quicinc.com>

---

### Thread 9: [PATCH 1/5] irqchip/gic-v5: Skip deactivate for forwarded PPI
 interrupts

**📧 邮件数**: 11 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 20 Jun 2025 16:07:50 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 GICv5 主机上支持 GICv3 客户机的补丁系列，主要集中在如何处理转发的 PPI 中断以及 GICv3 兼容模式的实现。

1. **原始补丁内容**：补丁的第一部分（[PATCH 1/5]）提出了在转发的 PPI 中断中跳过去激活（deactivate）操作，仅执行结束中断（EOI），依赖客户机在处理注入中断时自行处理虚拟和物理中断的去激活。这种做法模仿了原生 GICv3 的行为。

2. **之前讨论要点**：补丁系列的背景是为了在 GICv5 主机上实现 GICv3 客户机的支持，利用 GICv5 的遗留兼容性特性（FEAT_GCIE_LEGACY）。之前的讨论中提到，确保注入的客户机中断行为正确，并与 GICv3 的预期一致。

3. **本周的新讨论与进展**：本周的讨论中，参与者对补丁的实现细节进行了深入探讨，Oliver Upton 提出了对补丁的改进建议，包括合并某些功能以简化代码，并讨论了如何处理 GICv3 和 GICv5 的兼容性问题。此外，Sascha Bischoff 提出了补丁的总结和反馈请求，强调了对现有 GICv3 虚拟机的支持应无缝进行，而不需修改虚拟机或虚拟机监控器。

整体而言，本周的讨论推动了 GICv5 支持 GICv3 客户机的补丁系列的进一步完善，确保了兼容性和功能的有效实现。

#### 📝 邮件列表

1. **[06-20 16:07]** [PATCH 1/5] irqchip/gic-v5: Skip deactivate for forwarded PPI
 interrupts
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[06-20 16:07]** [PATCH 0/5] KVM: arm64: Enable GICv3 guests on GICv5 hosts using
 FEAT_GCIE_LEGACY
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
3. **[06-20 16:07]** [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
4. **[06-20 16:07]** [PATCH 3/5] arm64/sysreg: Add ICH_VCTLR_EL2
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
5. **[06-20 16:07]** [PATCH 2/5] irqchip/gic-v5: Populate struct gic_kvm_info
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
6. **[06-20 16:07]** [PATCH 5/5] KVM: arm64: gic-v5: Probe for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
7. **[06-20 13:20]** Re: [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[06-20 13:25]** Re: [PATCH 5/5] KVM: arm64: gic-v5: Probe for GICv5
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[06-20 16:02]** Re: [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[06-22 13:19]** Re: [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[06-22 05:37]** Re: [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 10: [PATCH v9 00/43] arm64: Support for Arm CCA in KVM

**📧 邮件数**: 10 | **👥 参与者**: 5 | **📅 开始时间**: Wed, 11 Jun 2025 11:47:57 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 Arm Confidential Compute Architecture (CCA) 的 KVM 支持的补丁系列（PATCH v9 00/43）。该补丁旨在实现受保护虚拟机的运行，相关的来宾支持已在 v6.14-rc1 中合并，因此不再需要单独处理。

在历史讨论中，Steven Price 提出了多个补丁，涵盖了创建和配置领域的 ioctl、RTT 的拆除、VMM 设置 RIPAS 的能力以及运行时内存故障处理等功能。这些补丁的主要改动包括简化 RTT 计数、处理 Realm 描述符的页面委托等。

在本周的新讨论中，参与者对补丁进行了细节上的审查和反馈。Suzuki K Poulose 提出了对代码注释的改进建议，以增强可读性。Gavin Shan 关注到在某些情况下可能导致 RCU 停滞的问题，并建议在调用 `kvm_stage2_unmap_range` 时设置 `may_block` 为 true。Yiwei Zhuang 询问是否需要在特定分支中释放和撤销 RTT，而 Andre Przywara 则报告了在 GCC 10 及以下版本中出现的构建错误，并建议调整变量声明的位置以解决问题。

总体来看，本周讨论集中在对补丁的细节审查和潜在问题的解决上，推动了补丁的进一步完善。

#### 📝 邮件列表

1. **[06-11 11:47]** [PATCH v9 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>
2. **[06-11 11:48]** [PATCH v9 07/43] arm64: RME: ioctls to create and configure realms
   - 发件人: Steven Price <steven.price@arm.com>
3. **[06-11 11:48]** [PATCH v9 10/43] arm64: RME: RTT tear down
   - 发件人: Steven Price <steven.price@arm.com>
4. **[06-11 11:48]** [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Steven Price <steven.price@arm.com>
5. **[06-11 11:48]** [PATCH v9 20/43] arm64: RME: Runtime faulting of memory
   - 发件人: Steven Price <steven.price@arm.com>
6. **[06-16 11:41]** Re: [PATCH v9 10/43] arm64: RME: RTT tear down
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
7. **[06-16 11:47]** Re: [PATCH v9 07/43] arm64: RME: ioctls to create and configure
 realms
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
8. **[06-16 21:55]** Re: [PATCH v9 20/43] arm64: RME: Runtime faulting of memory
   - 发件人: Gavin Shan <gshan@redhat.com>
9. **[06-17 20:56]** Re: [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: zhuangyiwei <zhuangyiwei@huawei.com>
10. **[06-18 13:33]** Re: [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Andre Przywara <andre.przywara@arm.com>

---

### Thread 11: [PATCH v8 0/6] KVM: arm64: Map GPU device memory as cacheable

**📧 邮件数**: 9 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 20 Jun 2025 12:09:40 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下如何将 GPU 设备内存映射为可缓存的内存。Ankit Agrawal 提出了一个包含六个补丁的系列更新，旨在解决当前 KVM 对设备内存映射的限制。

**原始补丁内容**：
补丁的核心目的是允许 GPU 设备内存被标记为可缓存。当前，KVM 只能将内存区域映射为 NORMAL 或 DEVICE_nGnRE，限制了未添加到内核的设备内存的缓存性。补丁通过检查 VMA（虚拟内存区域）的 pgprot 值来判断缓存性，从而实现更灵活的内存映射。

**之前讨论要点**：
在历史讨论中，维护者们对补丁进行了多次修改，提出了关于变量命名、代码结构和安全性检查的建议。补丁的设计考虑了多个硬件特性，如 S2FWB（强制写回）和 ARM64_HAS_CACHE_DIC，以确保缓存管理的安全性。

**本周的新讨论与进展**：
本周的讨论集中在补丁的具体实现上。Ankit 提出了多个补丁，涵盖了变量重命名、设备内存检测、缓存 PFNMAP 映射的阻止机制等。Jason Gunthorpe 提出了一些逻辑上的改进建议，认为某些检查可以简化。Ankit 同意进行相应的修改，并表示将进一步确认 COW（写时复制）映射的相关问题。

总体而言，这一系列补丁的目标是提升 KVM 对 GPU 设备内存的支持，确保其在虚拟化环境中的有效性和安全性。

#### 📝 邮件列表

1. **[06-20 12:09]** [PATCH v8 0/6] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: ankita <ankita@nvidia.com>
2. **[06-20 12:09]** [PATCH v8 1/6] KVM: arm64: Rename the device variable to s2_force_noncacheable
   - 发件人: ankita <ankita@nvidia.com>
3. **[06-20 12:09]** [PATCH v8 2/6] KVM: arm64: Update the check to detect device memory
   - 发件人: ankita <ankita@nvidia.com>
4. **[06-20 12:09]** [PATCH v8 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: ankita <ankita@nvidia.com>
5. **[06-20 12:09]** [PATCH v8 4/6] KVM: arm64: New function to determine hardware cache management support
   - 发件人: ankita <ankita@nvidia.com>
6. **[06-20 12:09]** [PATCH v8 5/6] KVM: arm64: Allow cacheable stage 2 mapping using VMA flags
   - 发件人: ankita <ankita@nvidia.com>
7. **[06-20 12:09]** [PATCH v8 6/6] KVM: arm64: Expose new KVM cap for cacheable PFNMAP
   - 发件人: ankita <ankita@nvidia.com>
8. **[06-20 09:20]** Re: [PATCH v8 5/6] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Jason Gunthorpe <jgg@nvidia.com>
9. **[06-20 13:07]** Re: [PATCH v8 5/6] KVM: arm64: Allow cacheable stage 2 mapping using
 VMA flags
   - 发件人: Ankit Agrawal <ankita@nvidia.com>

---

### Thread 12: [PATCH 0/7] KVM: arm64: trap fixes and cleanup

**📧 邮件数**: 9 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 17 Jun 2025 14:37:11 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 trap 管理的修复和清理工作，包含七个补丁。

1. **原始补丁内容**：补丁系列旨在修复 KVM 在 VHE（Virtualization Host Extensions）模式下管理 traps 的一些问题，并进行相关的简化和清理。主要补丁包括修复调试寄存器操作、CPTR（Control Processor Trap Register）管理等。

2. **之前讨论要点**：在历史讨论中，Mark Rutland 提到他在处理其他修复时发现了与调试寄存器和 CPTR 相关的潜在问题，并与 Will Deacon 进行了相关讨论，提出了简化和清理的想法。

3. **本周的新讨论与进展**：本周的讨论中，Mark Rutland 提交了七个补丁，分别修复了调试寄存器的恢复、CPTR trap 的去激活、CPTR 操作的重组等。所有补丁经过轻量测试后，Marc Zyngier 已确认并应用了这些补丁，表示感谢。

整体来看，本次讨论集中在提高 KVM 在 arm64 上的稳定性和简化代码结构，确保在多层虚拟化环境下的 trap 管理正确性。

#### 📝 邮件列表

1. **[06-17 14:37]** [PATCH 0/7] KVM: arm64: trap fixes and cleanup
   - 发件人: Mark Rutland <mark.rutland@arm.com>
2. **[06-17 14:37]** [PATCH 1/7] KVM: arm64: VHE: Synchronize restore of host debug registers
   - 发件人: Mark Rutland <mark.rutland@arm.com>
3. **[06-17 14:37]** [PATCH 2/7] KVM: arm64: VHE: Synchronize CPTR trap deactivation
   - 发件人: Mark Rutland <mark.rutland@arm.com>
4. **[06-17 14:37]** [PATCH 3/7] KVM: arm64: Reorganise CPTR trap manipulation
   - 发件人: Mark Rutland <mark.rutland@arm.com>
5. **[06-17 14:37]** [PATCH 4/7] KVM: arm64: Remove ad-hoc CPTR manipulation from fpsimd_sve_sync()
   - 发件人: Mark Rutland <mark.rutland@arm.com>
6. **[06-17 14:37]** [PATCH 5/7] KVM: arm64: Remove ad-hoc CPTR manipulation from kvm_hyp_handle_fpsimd()
   - 发件人: Mark Rutland <mark.rutland@arm.com>
7. **[06-17 14:37]** [PATCH 6/7] KVM: arm64: Remove cpacr_clear_set()
   - 发件人: Mark Rutland <mark.rutland@arm.com>
8. **[06-17 14:37]** [PATCH 7/7] KVM: arm64: VHE: Centralize ISBs when returning to host
   - 发件人: Mark Rutland <mark.rutland@arm.com>
9. **[06-19 13:36]** Re: [PATCH 0/7] KVM: arm64: trap fixes and cleanup
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 13: [PATCH v5 0/6] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI

**📧 邮件数**: 8 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 19 Jun 2025 09:02:53 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下支持 FF-A（Firmware Framework for Arm）1.2 及其 SEND_DIRECT2 ABI 的补丁集。该补丁集的主要目标是确保主机不会使用低于已与虚拟机监控器协商的 FF-A 版本，从而避免兼容性问题。

在历史讨论中，补丁集的背景是 FF-A 1.2 规范引入了新的 SEND_DIRECT2 ABI，允许使用 x4-x17 寄存器作为消息负载。补丁集还涉及对 SMCCC（Secure Monitor Call Convention）1.2 的支持，以便简化后续的接口实现。

本周的新讨论中，参与者 Per Larsen 提交了六个补丁，主要包括：
1. 修正主机版本降级尝试时的返回值。
2. 在 FF-A 初始化过程中使用 SMCCC 1.2。
3. 在主机 FF-A 处理程序中使用 SMCCC 1.2。
4. 将 FFA_NOTIFICATION_* 接口标记为不支持。
5. 将支持的 FF-A 版本提升至 1.2。
6. 在主机处理程序中支持 FFA_MSG_SEND_DIRECT_REQ2。

此外，Marc Zyngier 对补丁中的变量命名和代码重复提出了批评，认为这种改动增加了代码的复杂性，建议保持变量命名的一致性以提高可读性。整体来看，补丁集旨在提升 FF-A 的功能和兼容性，同时也引发了对代码可维护性的讨论。

#### 📝 邮件列表

1. **[06-19 09:02]** [PATCH v5 0/6] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[06-19 09:02]** [PATCH v5 1/6] KVM: arm64: Correct return value on host version
 downgrade attempt
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[06-19 09:02]** [PATCH v5 2/6] KVM: arm64: Use SMCCC 1.2 in
 hyp_ffa_{init,post_init}
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
4. **[06-19 09:02]** [PATCH v5 3/6] KVM: arm64: Use SMCCC 1.2 in host FF-A handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
5. **[06-19 09:02]** [PATCH v5 4/6] KVM: arm64: Mark FFA_NOTIFICATION_* calls as
 unsupported
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
6. **[06-19 09:02]** [PATCH v5 5/6] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
7. **[06-19 09:02]** [PATCH v5 6/6] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
8. **[06-22 14:01]** Re: [PATCH v5 3/6] KVM: arm64: Use SMCCC 1.2 in host FF-A handler
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 14: [PATCH kvmtool 0/3] arm64: Nested virtualization support

**📧 邮件数**: 8 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 20 Jun 2025 11:44:51 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的嵌套虚拟化支持的补丁（PATCH kvmtool 0/3）。该补丁的主要内容包括三个部分：更新内核头文件以支持新的 EL2 功能、引入新的命令行选项“--nested”以允许 VCPU 在 EL2 中启动，以及通过设置维护 IRQ 来支持 VGIC 设备。

在历史讨论中，参与者们对嵌套虚拟化的必要性进行了强调，Marc Zyngier 提到其他补丁（如 HYP 定时器 IRQ 和 E2H0）也很重要，建议将其作为其他虚拟机管理程序的模板。

本周的新讨论中，Andre Przywara 提供了补丁的详细信息，确认在 FVP 和一些商业硬件上进行了测试。Alexandru Elisei 提出将命令行选项“--nested”改为“--el2”的建议，以便与 KVM 的命名保持一致，但 Marc Zyngier 认为“nested”更能准确描述该功能的效果。最终，Alex 表示理解了 Marc 的观点，认为“--nested”选项是合适的。

总体来看，本周的讨论推动了补丁的完善，并对命令行选项的命名进行了深入探讨，确保了嵌套虚拟化支持的实施更加清晰和一致。

#### 📝 邮件列表

1. **[06-20 11:44]** [PATCH kvmtool 0/3] arm64: Nested virtualization support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
2. **[06-20 11:44]** [PATCH kvmtool 1/3] Sync kernel UAPI headers with v6.16-rc1
   - 发件人: Andre Przywara <andre.przywara@arm.com>
3. **[06-20 11:44]** [PATCH kvmtool 2/3] arm64: Initial nested virt support
   - 发件人: Andre Przywara <andre.przywara@arm.com>
4. **[06-20 11:44]** [PATCH kvmtool 3/3] arm64: nested: add support for setting maintenance IRQ
   - 发件人: Andre Przywara <andre.przywara@arm.com>
5. **[06-20 12:09]** Re: [PATCH kvmtool 2/3] arm64: Initial nested virt support
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
6. **[06-20 12:13]** Re: [PATCH kvmtool 0/3] arm64: Nested virtualization support
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[06-20 12:52]** Re: [PATCH kvmtool 2/3] arm64: Initial nested virt support
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[06-20 14:43]** Re: [PATCH kvmtool 2/3] arm64: Initial nested virt support
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

### Thread 15: [PATCH] KVM: arm64: nv: Fix s_cpu_if->vgic_lr[] indexing in vgic_v3_put_nested()

**📧 邮件数**: 8 | **👥 参与者**: 3 | **📅 开始时间**: Sat, 14 Jun 2025 22:57:21 +0800

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在修复 `vgic_v3_put_nested()` 函数中对 `s_cpu_if->vgic_lr[]` 索引的错误使用。

**原始补丁内容**：补丁由 Wei-Lin Chang 提出，主要修复了在 `vgic_v3_put_nested()` 函数中，`s_cpu_if->vgic_lr[]` 的索引方式不正确的问题。原本该数组应从索引 0 填充到 `s_cpu_if->used_lrs - 1`，但实际使用了 `shadow_if->lr_map` 中设置位的索引，导致了错误。

**之前讨论要点**：在补丁提出后，参与者对补丁的描述和实现进行了讨论。Oliver Upton 提出了对补丁描述的改进建议，Marc Zyngier 也指出了双重索引的脆弱性，建议进行代码重构以避免此类错误。

**本周新讨论与进展**：本周的讨论中，Marc Zyngier 提出了一个更全面的补丁，旨在通过消除双重索引来增强代码的健壮性。他建议直接使用 `lr_map` 中设置的位数来简化索引过程。Wei-Lin Chang 和 Oliver Upton 对此表示支持，并提出了函数命名的改进建议。最终，Marc Zyngier 更新了补丁，使用 `hweight16()` 替代 `hweight64()`，以优化性能并减少指令数量。整体上，讨论推动了补丁的完善和代码质量的提升。

#### 📝 邮件列表

1. **[06-14 22:57]** [PATCH] KVM: arm64: nv: Fix s_cpu_if->vgic_lr[] indexing in vgic_v3_put_nested()
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
2. **[06-15 22:55]** Re: [PATCH] KVM: arm64: nv: Fix s_cpu_if->vgic_lr[] indexing in
 vgic_v3_put_nested()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[06-16 11:54]** Re: [PATCH] KVM: arm64: nv: Fix s_cpu_if->vgic_lr[] indexing in vgic_v3_put_nested()
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[06-16 22:34]** Re: [PATCH] KVM: arm64: nv: Fix s_cpu_if->vgic_lr[] indexing in
 vgic_v3_put_nested()
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
5. **[06-16 22:40]** Re: [PATCH] KVM: arm64: nv: Fix s_cpu_if->vgic_lr[] indexing in
 vgic_v3_put_nested()
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
6. **[06-16 18:00]** Re: [PATCH] KVM: arm64: nv: Fix s_cpu_if->vgic_lr[] indexing in vgic_v3_put_nested()
   - 发件人: Marc Zyngier <maz@kernel.org>
7. **[06-16 21:53]** Re: [PATCH] KVM: arm64: nv: Fix s_cpu_if->vgic_lr[] indexing in
 vgic_v3_put_nested()
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[06-17 10:26]** Re: [PATCH] KVM: arm64: nv: Fix s_cpu_if->vgic_lr[] indexing in vgic_v3_put_nested()
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 16: [PATCH v9 0/6] KVM: arm64: Map GPU device memory as cacheable

**📧 邮件数**: 7 | **👥 参与者**: 1 | **📅 开始时间**: Sat, 21 Jun 2025 04:21:05 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下支持将 GPU 设备内存映射为可缓存的补丁（PATCH v9 0/6）。该补丁的主要目的是解决当前 KVM 强制将内存映射为 NORMAL 或 DEVICE_nGnRE 的限制，使得未添加到内核的设备内存也能被标记为可缓存。

在历史讨论中，参与者们关注了 GPU 设备内存的特性，如缓存性、未对齐访问、原子操作等，强调了将设备内存映射为 NORMAL 的必要性。补丁的设计受到多位维护者的建议影响，确保了安全性和性能。

本周的新讨论中，Ankit Agrawal 提出了六个补丁，具体进展包括：
1. 重命名了设备变量以更好地反映其功能。
2. 更新了检测设备内存的检查逻辑。
3. 阻止了缓存 PFNMAP 映射，解决了 S1 和 S2 映射属性不匹配的安全问题。
4. 引入了新的函数以确定硬件缓存管理支持。
5. 允许使用 VMA 标志进行可缓存的二级映射。
6. 暴露了新的 KVM 能力，以便用户空间检测是否支持缓存 PFNMAP。

这些补丁的实施将提高 KVM 对 GPU 设备内存的支持，增强虚拟化性能。

#### 📝 邮件列表

1. **[06-21 04:21]** [PATCH v9 0/6] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: ankita <ankita@nvidia.com>
2. **[06-21 04:21]** [PATCH v9 1/6] KVM: arm64: Rename the device variable to s2_force_noncacheable
   - 发件人: ankita <ankita@nvidia.com>
3. **[06-21 04:21]** [PATCH v9 2/6] KVM: arm64: Update the check to detect device memory
   - 发件人: ankita <ankita@nvidia.com>
4. **[06-21 04:21]** [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: ankita <ankita@nvidia.com>
5. **[06-21 04:21]** [PATCH v9 4/6] KVM: arm64: New function to determine hardware cache management support
   - 发件人: ankita <ankita@nvidia.com>
6. **[06-21 04:21]** [PATCH v9 5/6] KVM: arm64: Allow cacheable stage 2 mapping using VMA flags
   - 发件人: ankita <ankita@nvidia.com>
7. **[06-21 04:21]** [PATCH v9 6/6] KVM: arm64: Expose new KVM cap for cacheable PFNMAP
   - 发件人: ankita <ankita@nvidia.com>

---

### Thread 17: [PATCH 0/8] KVM: Remove include/kvm, standardize includes

**📧 邮件数**: 7 | **👥 参与者**: 4 | **📅 开始时间**: Tue, 10 Jun 2025 17:10:34 -0700

#### 🤖 AI 总结

本邮件线程讨论了一个关于KVM（Kernel-based Virtual Machine）的补丁系列，主要目的是移除`include/kvm`目录并标准化各架构的包含文件。

**原始补丁内容**：补丁系列的核心是通过文件移动和重命名来删除`include/kvm`，并在所有架构中标准化KVM的包含文件。这一改动与Colton的分区PMU系列存在冲突，但被认为是为分区PMU工作做的良好准备。

**之前讨论要点**：历史邮件中，Sean Christopherson提出了多个补丁，包括将ARM特定的头文件移动到架构目录、将`iodev.h`移至标准的`include/linux`目录，以及停止在PPC架构的包含路径中添加`virt/kvm`。这些补丁得到了Anup Patel的确认和支持。

**本周的新讨论与进展**：在本周的讨论中，Bibo Mao和Gautam Menghani分别对补丁4和补丁6进行了审核并表示认可。Zenghui Yu则指出，KVM/arm64的MAINTAINERS条目中与ARM相关的条目可以删除，进一步推动了补丁的清理工作。

总体来看，本周的讨论表明补丁系列正在获得积极的反馈，且逐步朝着标准化的目标迈进。

#### 📝 邮件列表

1. **[06-10 17:10]** [PATCH 0/8] KVM: Remove include/kvm, standardize includes
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[06-10 17:10]** [PATCH 3/8] KVM: arm64: Move ARM specific headers in include/kvm to
 arch directory
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[06-10 17:10]** [PATCH 4/8] KVM: Move include/kvm/iodev.h to include/linux as kvm_iodev.h
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[06-10 17:10]** [PATCH 6/8] KVM: PPC: Stop adding virt/kvm to the arch include path
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[06-16 09:13]** Re: [PATCH 4/8] KVM: Move include/kvm/iodev.h to include/linux as
 kvm_iodev.h
   - 发件人: Bibo Mao <maobibo@loongson.cn>
6. **[06-16 12:45]** Re: [PATCH 6/8] KVM: PPC: Stop adding virt/kvm to the arch include
 path
   - 发件人: Gautam Menghani <gautam@linux.ibm.com>
7. **[06-16 19:10]** Re: [PATCH 3/8] KVM: arm64: Move ARM specific headers in include/kvm
 to arch directory
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>

---

### Thread 18: [PATCH v3 0/4] KVM: arm64: Add attribute to control GICD_TYPER2.nASSGIcap

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 13 Jun 2025 15:52:34 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 的一个补丁，旨在为 arm64 架构添加一个属性，以控制 GICD_TYPER2.nASSGIcap 的功能。该补丁的目的是解决 GIC 架构在 ITS 中对虚拟处理单元（vPE）数量的限制，使得用户能够在每个虚拟机（VM）基础上控制该特性，从而为特定类型的 VM 提供硬件中断注入支持。

在历史讨论中，Raghavendra Rao Ananta 提出了该补丁的背景，强调了在 GICv4.1 系统中，KVM 默认会无条件支持 GICD_TYPER2.nASSGIcap，而补丁允许用户在 VGIC 初始化之前更改 VM 是否支持该特性，以便在资源受限的环境中更灵活地管理 vPE 的分配。

在本周的新讨论中，Marc Zyngier 提出了对补丁的建议，要求补充关于默认行为的说明，并质疑在没有 GICv4.1 的情况下是否仍应宣传 KVM_DEV_ARM_VGIC_FEATURE_nASSGIcap 的可配置性。他认为该 API 应该能够向后兼容旧版本的 KVM，并希望在补丁中明确这一点。

#### 📝 邮件列表

1. **[06-13 15:52]** [PATCH v3 0/4] KVM: arm64: Add attribute to control GICD_TYPER2.nASSGIcap
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
2. **[06-13 15:52]** [PATCH v3 3/4] KVM: arm64: Introduce attribute to control GICD_TYPER2.nASSGIcap
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
3. **[06-21 09:50]** Re: [PATCH v3 3/4] KVM: arm64: Introduce attribute to control GICD_TYPER2.nASSGIcap
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 19: [PATCH] KVM: arm64: Remove kvm_arch_vcpu_run_map_fp()

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Thu, 19 Jun 2025 14:48:17 +0100

#### 🤖 AI 总结

本邮件线程讨论的主题是关于移除 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 `kvm_arch_vcpu_run_map_fp()` 函数的补丁。该补丁的提出是基于历史上 KVM hyp 代码需要将主机的 FPSIMD 状态保存到主机的 `fpsimd_state` 内存中，并在运行 vCPU 之前将其映射到 hyp Stage-1 中。然而，随着最近的两个提交（`fbc7e61195e2` 和 `8eca7f6d5100`），这种映射已不再必要，因为在调用 hyp 运行 vCPU 之前，主机的 FPSIMD 状态会被主动保存，并且 hyp 代码不再读取或写入主机的 `fpsimd_state` 内存。因此，`kvm_arch_vcpu_run_map_fp()` 函数被认为是多余的。

在本周的新讨论中，Mark Rutland 提出了该补丁，并详细说明了移除该函数的原因。Fuad Tabba 和 Mark Brown 对该补丁进行了测试和审核，均表示支持并确认其有效性。整体来看，本周的讨论集中在补丁的确认和审核上，表明该补丁即将被合并。

#### 📝 邮件列表

1. **[06-19 14:48]** [PATCH] KVM: arm64: Remove kvm_arch_vcpu_run_map_fp()
   - 发件人: Mark Rutland <mark.rutland@arm.com>
2. **[06-19 15:35]** Re: [PATCH] KVM: arm64: Remove kvm_arch_vcpu_run_map_fp()
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[06-19 17:28]** Re: [PATCH] KVM: arm64: Remove kvm_arch_vcpu_run_map_fp()
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 20: [PATCH v6 3/5] kvm: arm64: New memslot flag to indicate cacheable mapping

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 6 Jun 2025 10:57:34 -0700

#### 🤖 AI 总结

在本次邮件讨论中，主题为“[PATCH v6 3/5] kvm: arm64: 新的内存槽标志以指示可缓存映射”。该补丁旨在为 KVM（内核虚拟机）引入一个新的内存槽标志，以支持可缓存的物理页框映射。

在历史讨论中，Sean Christopherson 和 Oliver Upton 对该补丁提出了批评。Sean 指出，该实现不应包含在 KVM 的用户空间 API 中，并认为当前的设计存在混乱，尤其是 x86 架构对可缓存 PFNMAP 映射的支持问题。Oliver 也表示，用户空间需要了解其在阶段 1 中的内容，以便更好地理解该标志的意义，并提到需要更细粒度的枚举来适应架构的实现。

在本周的新讨论中，Ankit Agrawal 感谢了 Sean、Jason 和 Oliver 的反馈，并决定删除该标志，同时在下一个版本中继续保留 KVM 的能力。这表明对之前讨论的反馈进行了积极响应，并计划在后续版本中进行调整。

#### 📝 邮件列表

1. **[06-06 10:57]** Re: [PATCH v6 3/5] kvm: arm64: New memslot flag to indicate cacheable mapping
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[06-13 12:38]** Re: [PATCH v6 3/5] kvm: arm64: New memslot flag to indicate
 cacheable mapping
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[06-16 11:37]** Re: [PATCH v6 3/5] kvm: arm64: New memslot flag to indicate cacheable
 mapping
   - 发件人: Ankit Agrawal <ankita@nvidia.com>

---

### Thread 21: [PATCH] KVM: arm64: selftests: Close the GIC FD in arch_timer_edge_cases

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Sun, 8 Jun 2025 17:54:02 +0800

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的自测试补丁。补丁的主要内容是关闭 GIC（通用中断控制器）文件描述符，以释放其对虚拟机的引用，从而确保可以正确清理虚拟机，并消除在运行 arch_timer_edge_cases 测试时出现的重复目录警告。

在历史讨论中，Zenghui Yu 提出了这个补丁，并详细说明了其目的和修改内容，包括在相关源文件中进行的具体代码更改。

在本周的新讨论中，Marc Zyngier 对该补丁表示感谢，并确认已将其应用到修复列表中。这表明补丁得到了认可并已被纳入代码库，标志着该问题的解决进展。整体来看，此次讨论围绕着提升 KVM 自测试的稳定性和清理过程的有效性展开。

#### 📝 邮件列表

1. **[06-08 17:54]** [PATCH] KVM: arm64: selftests: Close the GIC FD in arch_timer_edge_cases
   - 发件人: Zenghui Yu <yuzenghui@huawei.com>
2. **[06-19 13:36]** Re: [PATCH] KVM: arm64: selftests: Close the GIC FD in arch_timer_edge_cases
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 22: [PATCH v2 09/14] mips: Handle KCOV __init vs inline mismatches

**📧 邮件数**: 2 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 19 Jun 2025 16:55:15 +0800

#### 🤖 AI 总结

本邮件线程讨论了一个针对 MIPS 架构的补丁（patch），主题为“处理 KCOV 的 __init 与 inline 不匹配问题”。该补丁的主要目的是解决 MIPS 架构在 KCOV 功能实现中，__init 和 __always_inline 标记的不一致性。

在历史讨论中，虽然没有具体的邮件记录，但可以推测之前的讨论围绕如何在 MIPS 架构中有效地使用这些标记，以确保代码的正确性和性能。Kees Cook 提出了将某些函数标记为 __init，而不是 __always_inline，以与 x86 和 ARM 架构保持一致。

在本周的新讨论中，Huacai Chen 对 Kees Cook 的观点表示支持，重申了将相关函数标记为 __init 的优先选择。这表明参与者在补丁的方向上达成了一致意见，进一步推动了补丁的实施。

总体来看，本周的讨论主要集中在补丁的标记选择上，参与者们倾向于采用与其他架构一致的做法，以提高代码的可维护性和兼容性。

#### 📝 邮件列表

1. **[06-19 16:55]** Re: [PATCH v2 09/14] mips: Handle KCOV __init vs inline mismatches
   - 发件人: Huacai Chen <chenhuacai@kernel.org>
2. **[06-19 16:55]** Re: [PATCH v2 10/14] loongarch: Handle KCOV __init vs inline mismatches
   - 发件人: Huacai Chen <chenhuacai@kernel.org>

---

## 📌 RFC

共 2 个 thread

---

### Thread 1: [RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 19 Jun 2025 15:10:15 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）中嵌套虚拟化自测试的补丁（RFC PATCH v2 0/9）。该补丁旨在启用嵌套虚拟化的自测试功能，以便更好地验证和测试虚拟化环境的稳定性和性能。

在历史讨论中，参与者们探讨了补丁的基本结构和实现细节，特别是如何在不同的执行级别（EL）下运行自测试代码。Marc Zyngier 提到，默认的测试代码在 EL2 中运行，并且启用了 E2H（Exception Level to Hypervisor）。此外，讨论中提到 L1 和 L2 虚拟机之间的切换问题，但并未深入解决。

在本周的新讨论中，Ganapatrao Kulkarni 和 Marc Zyngier 继续探讨了自测试的具体实现。Ganapatrao 提出，当前的测试需要在完整的客操作系统上运行，这可能不够高效。他强调需要合成测试，以实现整个虚拟化堆栈的验证，包括多个层级的虚拟机（L1、L2、L3）。Marc Zyngier 对此表示困惑，并质疑这种方法的实际意义，认为应该专注于更有效的测试策略。

总结来看，本周的讨论集中在如何优化嵌套虚拟化自测试的实施上，参与者们对测试的有效性和实现方式提出了不同的看法。

#### 📝 邮件列表

1. **[06-19 15:10]** Re: [RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
2. **[06-19 12:45]** Re: [RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [RFC PATCH 00/34] Running Qualcomm's Gunyah Guests via KVM in
 EL1

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 19 Jun 2025 16:50:29 +0100

#### 🤖 AI 总结

本邮件主题为“[RFC PATCH 00/34] 通过 KVM 在 EL1 中运行 Qualcomm 的 Gunyah Guests”，主要讨论了在 ARM 架构下如何实现对 Gunyah Guests 的支持。

在历史讨论中，虽然没有具体的邮件记录，但可以推测出该补丁旨在扩展 KVM 的功能，以支持 Qualcomm 的 Gunyah 虚拟化技术。Marc Zyngier 提出，内核的目标是为所有硬件提供一致的用户空间 API，因此在虚拟化方面也应如此。如果内核无法提供支持所有类型虚拟化的 API，那么就意味着设计上存在问题。

在本周的新讨论中，David Woodhouse 对 Marc 的观点进行了回应，强调了内核在虚拟化支持方面的重要性。他指出，类似于 x86 架构下的 /dev/kvm 支持不同厂商的特性，ARM 架构也不应例外，内核应当能够支持各种虚拟化需求，而不是简单地拒绝某些功能的实现。

总体来看，本周的讨论进一步强调了在 ARM 上实现全面虚拟化支持的必要性，并对当前补丁的方向进行了积极的探讨。

#### 📝 邮件列表

1. **[06-19 16:50]** Re: [RFC PATCH 00/34] Running Qualcomm's Gunyah Guests via KVM in
 EL1
   - 发件人: David Woodhouse <dwmw2@infradead.org>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fixes, take #3

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 19 Jun 2025 14:00:49 +0100

#### 🤖 AI 总结

本邮件讨论主题为 KVM/arm64 修复的第三批更新，主要涉及 Linux 6.16 版本的修复内容。

1. **原始 patch/问题的内容**：本次 patch 包含了一系列针对 KVM/arm64 的修复，特别是 FP/SVE 相关的 bug 修复，解决了与 NV 相关的问题，并修补了一些缺失的同步机制。此外，还涉及中断处理、影子链接寄存器的错误处理以及自测修复。

2. **之前的讨论要点**：在本次邮件之前并没有相关的历史讨论记录，因此没有提供额外的背景信息。

3. **本周的新讨论、进展或结论**：本周的讨论主要由 Marc Zyngier 提出，详细列出了修复的具体内容，包括对 FP/SIMD/SVE bug 的修复、IRQ bypass 钩子的改进、影子链接寄存器的处理重构，以及对 arch_timer_edge_cases 自测的修复。Paolo Bonzini 对此进行了确认并表示感谢，表示已完成处理。

总体来看，本周的讨论集中在 KVM/arm64 的修复上，确保了系统的稳定性和性能。

#### 📝 邮件列表

1. **[06-19 14:00]** [GIT PULL] KVM/arm64 fixes, take #3
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[06-20 19:09]** Re: [GIT PULL] KVM/arm64 fixes, take #3
   - 发件人: Paolo Bonzini <pbonzini@redhat.com>

---

## 📌 Discussion

共 1 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v2 0/9] arm64: support EL2

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 16 Jun 2025 13:34:17 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM 单元测试的补丁，主题为“arm64: support EL2”。该补丁包含 9 个部分，旨在为 ARM64 架构提供对 EL2 的支持。

在历史讨论中，补丁的背景和目的并未详细列出，但可以推测，补丁的核心问题在于如何正确初始化 EL2，并确保与 KVM 的兼容性。

本周的新讨论中，参与者 Alexandru Elisei 和 Joey Gouly 进行了深入交流。Alexandru 指出，当前代码在处理 FEAT_E2H0 时存在缺陷，建议考虑直接使用现有的 el2_setup.h 文件中的部分代码，而不是重新编写初始化代码。他认为这样可以简化后续的更新和修复工作。Joey 对此表示赞同，并提到 INIT_HCR_EL2_EL1_ONLY 仅在不支持 VHE 的情况下使用，并确认补丁的第 9 部分对此进行了处理。他还表示将考虑基于 Linux 的代码创建一个简化版的 el2_setup.h。

总结而言，本周的讨论集中在如何优化 EL2 初始化代码的实现上，双方达成了一致意见，认为共享已有代码将有助于提高效率。

#### 📝 邮件列表

1. **[06-16 13:34]** Re: [kvm-unit-tests PATCH v2 0/9] arm64: support EL2
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[06-17 13:49]** Re: [kvm-unit-tests PATCH v2 0/9] arm64: support EL2
   - 发件人: Joey Gouly <joey.gouly@arm.com>

---

