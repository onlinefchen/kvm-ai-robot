# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-12-22 00:25:26

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 298
- **总 Thread 数**: 26
- **大型 Thread** (>20封): 4 个

### 分类分布

- **PATCH**: 16 threads (283 邮件)
- **RFC**: 6 threads (7 邮件)
- **Bug Report**: 2 threads (3 邮件)
- **Discussion**: 1 threads (4 邮件)
- **Other**: 1 threads (1 邮件)

---

## 📌 PATCH

共 16 个 thread

---

### Thread 1: [PATCH v12 00/46] arm64: Support for Arm CCA in KVM

**📧 邮件数**: 54 | **👥 参与者**: 4 | **📅 开始时间**: Wed, 17 Dec 2025 10:10:37 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM CCA（Confidential Compute Architecture）在 KVM（Kernel-based Virtual Machine）中的支持，主要集中在一系列补丁（PATCH v12 00/46）上，这些补丁涉及到如何在 KVM 中实现对受保护虚拟机的支持。

1. **原始补丁/问题内容**：补丁系列旨在为 KVM 添加对 ARM CCA 的支持，允许在受保护的环境中运行虚拟机。补丁中对用户 API 进行了调整，以简化虚拟机管理程序（VMM）在构建领域时的操作。

2. **之前讨论要点**：之前的讨论主要集中在如何实现和测试这些补丁的有效性，包括对 RMM（Realm Management Monitor）版本的兼容性、性能改进以及如何处理不同的中断和计时器等问题。

3. **本周的新讨论、进展或结论**：本周的讨论中，补丁的具体实现细节得到了进一步的完善，包括：
   - 对 RMM 的支持和如何在 VCPU 运行时激活领域。
   - 增加了对 PSCI（Power State Coordination Interface）请求的处理。
   - 讨论了如何在用户空间中注入异常和处理 MMIO（内存映射输入输出）操作。
   - 引入了对 SVE（Scalable Vector Extension）支持的检查，并更新了相关的寄存器列表。
   - 通过补丁 46，确认了在检测到 RMM 后启用 KVM 的领域支持。

整体来看，这些补丁的实现为在 KVM 中支持 ARM CCA 提供了基础，允许更安全的虚拟化环境。

#### 📝 邮件列表

1. **[12-17 10:10]** [PATCH v12 00/46] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>
2. **[12-17 10:10]** [PATCH v12 01/46] kvm: arm64: Include kvm_emulate.h in kvm/arm_psci.h
   - 发件人: Steven Price <steven.price@arm.com>
3. **[12-17 10:10]** [PATCH v12 02/46] arm64: RME: Handle Granule Protection Faults (GPFs)
   - 发件人: Steven Price <steven.price@arm.com>
4. **[12-17 10:10]** [PATCH v12 03/46] arm64: RMI: Add SMC definitions for calling the RMM
   - 发件人: Steven Price <steven.price@arm.com>
5. **[12-17 10:10]** [PATCH v12 04/46] arm64: RMI: Add wrappers for RMI calls
   - 发件人: Steven Price <steven.price@arm.com>
6. **[12-17 10:10]** [PATCH v12 05/46] arm64: RMI: Check for RMI support at KVM init
   - 发件人: Steven Price <steven.price@arm.com>
7. **[12-17 10:10]** [PATCH v12 06/46] arm64: RMI: Define the user ABI
   - 发件人: Steven Price <steven.price@arm.com>
8. **[12-17 10:10]** [PATCH v12 07/46] arm64: RMI: Basic infrastructure for creating a realm.
   - 发件人: Steven Price <steven.price@arm.com>
9. **[12-17 10:10]** [PATCH v12 08/46] kvm: arm64: Don't expose unsupported capabilities for realm guests
   - 发件人: Steven Price <steven.price@arm.com>
10. **[12-17 10:10]** [PATCH v12 09/46] KVM: arm64: Allow passing machine type in KVM creation
   - 发件人: Steven Price <steven.price@arm.com>
11. **[12-17 10:10]** [PATCH v12 10/46] arm64: RMI: RTT tear down
   - 发件人: Steven Price <steven.price@arm.com>
12. **[12-17 10:10]** [PATCH v12 11/46] arm64: RMI: Activate realm on first VCPU run
   - 发件人: Steven Price <steven.price@arm.com>
13. **[12-17 10:10]** [PATCH v12 12/46] arm64: RMI: Allocate/free RECs to match vCPUs
   - 发件人: Steven Price <steven.price@arm.com>
14. **[12-17 10:10]** [PATCH v12 13/46] KVM: arm64: vgic: Provide helper for number of list registers
   - 发件人: Steven Price <steven.price@arm.com>
15. **[12-17 10:10]** [PATCH v12 14/46] arm64: RMI: Support for the VGIC in realms
   - 发件人: Steven Price <steven.price@arm.com>
16. **[12-17 10:10]** [PATCH v12 15/46] KVM: arm64: Support timers in realm RECs
   - 发件人: Steven Price <steven.price@arm.com>
17. **[12-17 10:10]** [PATCH v12 16/46] arm64: RMI: Handle realm enter/exit
   - 发件人: Steven Price <steven.price@arm.com>
18. **[12-17 10:10]** [PATCH v12 17/46] arm64: RMI: Handle RMI_EXIT_RIPAS_CHANGE
   - 发件人: Steven Price <steven.price@arm.com>
19. **[12-17 10:10]** [PATCH v12 18/46] KVM: arm64: Handle realm MMIO emulation
   - 发件人: Steven Price <steven.price@arm.com>
20. **[12-17 10:10]** [PATCH v12 19/46] KVM: arm64: Expose support for private memory
   - 发件人: Steven Price <steven.price@arm.com>
21. **[12-17 10:10]** [PATCH v12 20/46] arm64: RMI: Allow populating initial contents
   - 发件人: Steven Price <steven.price@arm.com>
22. **[12-17 10:10]** [PATCH v12 21/46] arm64: RMI: Set RIPAS of initial memslots
   - 发件人: Steven Price <steven.price@arm.com>
23. **[12-17 10:10]** [PATCH v12 22/46] arm64: RMI: Create the realm descriptor
   - 发件人: Steven Price <steven.price@arm.com>
24. **[12-17 10:11]** [PATCH v12 23/46] arm64: RMI: Add a VMID allocator for realms
   - 发件人: Steven Price <steven.price@arm.com>
25. **[12-17 10:11]** [PATCH v12 24/46] arm64: RMI: Runtime faulting of memory
   - 发件人: Steven Price <steven.price@arm.com>
26. **[12-17 10:11]** [PATCH v12 25/46] KVM: arm64: Handle realm VCPU load
   - 发件人: Steven Price <steven.price@arm.com>
27. **[12-17 10:11]** [PATCH v12 26/46] KVM: arm64: Validate register access for a Realm VM
   - 发件人: Steven Price <steven.price@arm.com>
28. **[12-17 10:11]** [PATCH v12 27/46] KVM: arm64: Handle Realm PSCI requests
   - 发件人: Steven Price <steven.price@arm.com>
29. **[12-17 10:11]** [PATCH v12 28/46] KVM: arm64: WARN on injected undef exceptions
   - 发件人: Steven Price <steven.price@arm.com>
30. **[12-17 10:11]** [PATCH v12 29/46] arm64: Don't expose stolen time for realm guests
   - 发件人: Steven Price <steven.price@arm.com>
31. **[12-17 10:11]** [PATCH v12 30/46] arm64: RMI: allow userspace to inject aborts
   - 发件人: Steven Price <steven.price@arm.com>
32. **[12-17 10:11]** [PATCH v12 31/46] arm64: RMI: support RSI_HOST_CALL
   - 发件人: Steven Price <steven.price@arm.com>
33. **[12-17 10:11]** [PATCH v12 32/46] arm64: RMI: Allow checking SVE on VM instance
   - 发件人: Steven Price <steven.price@arm.com>
34. **[12-17 10:11]** [PATCH v12 33/46] arm64: RMI: Always use 4k pages for realms
   - 发件人: Steven Price <steven.price@arm.com>
35. **[12-17 10:11]** [PATCH v12 34/46] arm64: RMI: Prevent Device mappings for Realms
   - 发件人: Steven Price <steven.price@arm.com>
36. **[12-17 10:11]** [PATCH v12 35/46] HACK: Restore per-CPU cpu_armpmu pointer
   - 发件人: Steven Price <steven.price@arm.com>
37. **[12-17 10:11]** [PATCH v12 36/46] arm_pmu: Provide a mechanism for disabling the physical IRQ
   - 发件人: Steven Price <steven.price@arm.com>
38. **[12-17 10:11]** [PATCH v12 37/46] arm64: RMI: Enable PMU support with a realm guest
   - 发件人: Steven Price <steven.price@arm.com>
39. **[12-17 10:11]** [PATCH v12 38/46] arm64: RMI: Propagate number of breakpoints and watchpoints to userspace
   - 发件人: Steven Price <steven.price@arm.com>
40. **[12-17 10:11]** [PATCH v12 39/46] arm64: RMI: Set breakpoint parameters through SET_ONE_REG
   - 发件人: Steven Price <steven.price@arm.com>
41. **[12-17 10:11]** [PATCH v12 40/46] arm64: RMI: Initialize PMCR.N with number counter supported by RMM
   - 发件人: Steven Price <steven.price@arm.com>
42. **[12-17 10:11]** [PATCH v12 41/46] arm64: RMI: Propagate max SVE vector length from RMM
   - 发件人: Steven Price <steven.price@arm.com>
43. **[12-17 10:11]** [PATCH v12 42/46] arm64: RMI: Configure max SVE vector length for a Realm
   - 发件人: Steven Price <steven.price@arm.com>
44. **[12-17 10:11]** [PATCH v12 43/46] arm64: RMI: Provide register list for unfinalized RMI RECs
   - 发件人: Steven Price <steven.price@arm.com>
45. **[12-17 10:11]** [PATCH v12 44/46] arm64: RMI: Provide accurate register list
   - 发件人: Steven Price <steven.price@arm.com>
46. **[12-17 10:11]** [PATCH v12 45/46] KVM: arm64: Expose KVM_ARM_VCPU_REC to user space
   - 发件人: Steven Price <steven.price@arm.com>
47. **[12-17 10:11]** [PATCH v12 46/46] arm64: RMI: Enable realms to be created
   - 发件人: Steven Price <steven.price@arm.com>
48. **[12-17 14:29]** Re: [PATCH v12 11/46] arm64: RMI: Activate realm on first VCPU run
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
49. **[12-17 14:55]** Re: [PATCH v12 00/46] arm64: Support for Arm CCA in KVM
   - 发件人: Marc Zyngier <maz@kernel.org>
50. **[12-17 15:28]** Re: [PATCH v12 00/46] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>
51. **[12-20 21:46]** Re: [PATCH v12 19/46] KVM: arm64: Expose support for private memory
   - 发件人: kernel test robot <lkp@intel.com>
52. **[12-20 21:59]** Re: [PATCH v12 19/46] KVM: arm64: Expose support for private memory
   - 发件人: kernel test robot <lkp@intel.com>
53. **[12-20 15:18]** Re: [PATCH v12 19/46] KVM: arm64: Expose support for private memory
   - 发件人: kernel test robot <lkp@intel.com>
54. **[12-20 22:34]** Re: [PATCH v12 20/46] arm64: RMI: Allow populating initial contents
   - 发件人: kernel test robot <lkp@intel.com>

---

### Thread 2: [PATCH 00/32] KVM: arm64: Introduce vGIC-v5 with PPI support

**📧 邮件数**: 51 | **👥 参与者**: 6 | **📅 开始时间**: Fri, 12 Dec 2025 15:22:34 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下引入 vGIC-v5（虚拟通用中断控制器版本5）及其对 PPI（私有中断）的支持。

**原始 patch/问题的内容**：
Sascha Bischoff 提出的补丁系列（共32个补丁）旨在为 KVM 添加 vGIC-v5 设备的支持，初步实现仅支持 PPI，并计划在后续补丁中添加对 SPI（共享中断）和 LPI（本地中断）的支持。

**之前讨论要点**：
在历史讨论中，参与者们对补丁的实现细节进行了深入探讨，包括如何处理 GICv5 的中断类型、寄存器的生成、状态保存与恢复等。Marc Zyngier 提出了一些代码改进建议，并指出某些补丁的描述不够清晰。

**本周的新讨论、进展或结论**：
本周的讨论集中在补丁的具体实现和潜在问题上。kernel test robot 报告了一些构建警告，Sascha 表示将修复这些问题。此外，参与者们讨论了如何更好地处理 PPI 的注入和状态管理，Marc Zyngier 对某些实现细节提出了修改建议。Sascha 也对如何优化代码结构和提高可读性进行了反思，并表示将会在后续版本中进行改进。整体上，讨论氛围积极，参与者们对补丁的完善和功能实现充满期待。

#### 📝 邮件列表

1. **[12-12 15:22]** [PATCH 00/32] KVM: arm64: Introduce vGIC-v5 with PPI support
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[12-12 15:22]** [PATCH 02/32] KVM: arm64: gic-v3: Switch vGIC-v3 to use generated
 ICH_VMCR_EL2
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
3. **[12-12 15:22]** [PATCH 07/32] KVM: arm64: gic: Introduce interrupt type helpers
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
4. **[12-12 15:22]** [PATCH 09/32] KVM: arm64: gic-v5: Compute GICv5 FGTs on vcpu load
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
5. **[12-12 15:22]** [PATCH 10/32] KVM: arm64: gic-v5: Add emulation for ICC_IAFFID_EL1
 accesses
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
6. **[12-12 15:22]** [PATCH 13/32] KVM: arm64: gic-v5: Add vgic-v5 save/restore hyp
 interface
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
7. **[12-12 15:22]** [PATCH 11/32] KVM: arm64: gic-v5: Trap and emulate ICH_PPI_HMRx_EL1
 accesses
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
8. **[12-12 15:22]** [PATCH 14/32] KVM: arm64: gic-v5: Implement GICv5 load/put and
 save/restore
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
9. **[12-12 15:22]** [PATCH 16/32] KVM: arm64: gic: Introduce irq_queue and
 set_pending_state to irq_ops
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
10. **[12-12 15:22]** [PATCH 15/32] KVM: arm64: gic-v5: Implement direct injection of PPIs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
11. **[12-12 15:22]** [PATCH 17/32] KVM: arm64: gic-v5: Implement PPI interrupt injection
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
12. **[12-12 15:22]** [PATCH 19/32] KVM: arm64: gic-v5: Init Private IRQs (PPIs) for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
13. **[12-12 15:22]** [PATCH 18/32] KVM: arm64: gic-v5: Check for pending PPIs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
14. **[12-12 15:22]** [PATCH 23/32] KVM: arm64: gic-v5: Bump arch timer for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
15. **[12-12 15:22]** [PATCH 29/32] irqchip/gic-v5: Check if impl is virt capable
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
16. **[12-12 15:22]** [PATCH 31/32] Documentation: KVM: Introduce documentation for VGICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
17. **[12-12 16:24]** Re: [PATCH 09/32] KVM: arm64: gic-v5: Compute GICv5 FGTs on vcpu load
   - 发件人: Marc Zyngier <maz@kernel.org>
18. **[12-13 13:59]** Re: [PATCH 14/32] KVM: arm64: gic-v5: Implement GICv5 load/put and
 save/restore
   - 发件人: kernel test robot <lkp@intel.com>
19. **[12-15 01:15]** Re: [PATCH 31/32] Documentation: KVM: Introduce documentation for
 VGICv5
   - 发件人: kernel test robot <lkp@intel.com>
20. **[12-15 09:56]** Re: [PATCH 31/32] Documentation: KVM: Introduce documentation for VGICv5
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
21. **[12-15 10:54]** Re: [PATCH 14/32] KVM: arm64: gic-v5: Implement GICv5 load/put and
 save/restore
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
22. **[12-15 11:52]** Re: [PATCH 02/32] KVM: arm64: gic-v3: Switch vGIC-v3 to use generated ICH_VMCR_EL2
   - 发件人: Marc Zyngier <maz@kernel.org>
23. **[12-15 13:01]** Re: [PATCH 31/32] Documentation: KVM: Introduce documentation for
 VGICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
24. **[12-15 13:32]** Re: [PATCH 07/32] KVM: arm64: gic: Introduce interrupt type helpers
   - 发件人: Marc Zyngier <maz@kernel.org>
25. **[12-15 14:15]** Re: [PATCH 02/32] KVM: arm64: gic-v3: Switch vGIC-v3 to use generated
 ICH_VMCR_EL2
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
26. **[12-15 15:50]** Re: [PATCH 23/32] KVM: arm64: gic-v5: Bump arch timer for GICv5
   - 发件人: Marc Zyngier <maz@kernel.org>
27. **[12-15 16:01]** Re: [PATCH 07/32] KVM: arm64: gic: Introduce interrupt type helpers
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
28. **[12-15 16:05]** Re: [PATCH 07/32] KVM: arm64: gic: Introduce interrupt type helpers
   - 发件人: Marc Zyngier <maz@kernel.org>
29. **[12-15 17:31]** Re: [PATCH 10/32] KVM: arm64: gic-v5: Add emulation for ICC_IAFFID_EL1 accesses
   - 发件人: Marc Zyngier <maz@kernel.org>
30. **[12-15 17:37]** Re: [PATCH 09/32] KVM: arm64: gic-v5: Compute GICv5 FGTs on vcpu load
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
31. **[12-16 08:57]** Re: [PATCH 07/32] KVM: arm64: gic: Introduce interrupt type helpers
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
32. **[12-16 10:41]** Re: [PATCH 11/32] KVM: arm64: gic-v5: Trap and emulate ICH_PPI_HMRx_EL1 accesses
   - 发件人: Marc Zyngier <maz@kernel.org>
33. **[12-16 10:55]** Re: [PATCH 23/32] KVM: arm64: gic-v5: Bump arch timer for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
34. **[12-16 10:57]** Re: [PATCH 10/32] KVM: arm64: gic-v5: Add emulation for
 ICC_IAFFID_EL1 accesses
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
35. **[12-16 11:54]** Re: [PATCH 11/32] KVM: arm64: gic-v5: Trap and emulate
 ICH_PPI_HMRx_EL1 accesses
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
36. **[12-16 15:09]** Re: [PATCH 11/32] KVM: arm64: gic-v5: Trap and emulate ICH_PPI_HMRx_EL1 accesses
   - 发件人: Marc Zyngier <maz@kernel.org>
37. **[12-16 16:40]** Re: [PATCH 29/32] irqchip/gic-v5: Check if impl is virt capable
   - 发件人: Lorenzo Pieralisi <lpieralisi@kernel.org>
38. **[12-17 09:34]** Re: [PATCH 16/32] KVM: arm64: gic: Introduce irq_queue and set_pending_state to irq_ops
   - 发件人: Marc Zyngier <maz@kernel.org>
39. **[12-17 10:33]** Re: [PATCH 17/32] KVM: arm64: gic-v5: Implement PPI interrupt injection
   - 发件人: Marc Zyngier <maz@kernel.org>
40. **[12-17 11:07]** Re: [PATCH 13/32] KVM: arm64: gic-v5: Add vgic-v5 save/restore hyp interface
   - 发件人: Marc Zyngier <maz@kernel.org>
41. **[12-17 11:40]** Re: [PATCH 15/32] KVM: arm64: gic-v5: Implement direct injection of PPIs
   - 发件人: Marc Zyngier <maz@kernel.org>
42. **[12-17 11:49]** Re: [PATCH 18/32] KVM: arm64: gic-v5: Check for pending PPIs
   - 发件人: Joey Gouly <joey.gouly@arm.com>
43. **[12-17 12:00]** Re: [PATCH 18/32] KVM: arm64: gic-v5: Check for pending PPIs
   - 发件人: Joey Gouly <joey.gouly@arm.com>
44. **[12-17 14:29]** Re: [PATCH 18/32] KVM: arm64: gic-v5: Check for pending PPIs
   - 发件人: Marc Zyngier <maz@kernel.org>
45. **[12-17 15:54]** Re: [PATCH 17/32] KVM: arm64: gic-v5: Implement PPI interrupt
 injection
   - 发件人: Joey Gouly <joey.gouly@arm.com>
46. **[12-17 17:13]** Re: [PATCH 19/32] KVM: arm64: gic-v5: Init Private IRQs (PPIs) for GICv5
   - 发件人: Marc Zyngier <maz@kernel.org>
47. **[12-17 20:46]** Re: [PATCH 29/32] irqchip/gic-v5: Check if impl is virt capable
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
48. **[12-17 20:50]** Re: [PATCH 16/32] KVM: arm64: gic: Introduce irq_queue and
 set_pending_state to irq_ops
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
49. **[12-17 21:10]** Re: [PATCH 17/32] KVM: arm64: gic-v5: Implement PPI interrupt
 injection
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
50. **[12-17 21:42]** Re: [PATCH 13/32] KVM: arm64: gic-v5: Add vgic-v5 save/restore hyp
 interface
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
51. **[12-18 08:17]** Re: [PATCH 18/32] KVM: arm64: gic-v5: Check for pending PPIs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>

---

### Thread 3: [PATCH v2 00/45] arm_mpam: Add KVM/arm64 and resctrl glue code

**📧 邮件数**: 48 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 19 Dec 2025 18:11:02 +0000

#### 🤖 AI 总结

本邮件线程讨论了关于 ARM MPAM（内存系统资源分区和监控）与 resctrl（资源控制）集成的补丁系列，主要集中在 KVM（虚拟机监控器）和资源监控的实现细节。

1. **原始补丁内容**：
   - 本次补丁系列（[PATCH v2 00/45]）旨在为 ARM MPAM 添加 KVM 和 resctrl 的支持，解决了之前版本中的一些缺失部分。补丁涉及对 MPAM 控制寄存器的处理、KVM 部分的重构、以及一些小的 bug 修复。

2. **历史讨论要点**：
   - 之前的讨论主要集中在如何将 MPAM 的功能与 resctrl 结合，以便在用户空间和内核空间中有效管理资源。补丁中提到的 MPAM 设置在内核和用户空间中是共享的，这样可以避免用户空间绕过 MPAM 控制的情况。

3. **本周新讨论与进展**：
   - 本周的讨论中，Ben Horgan 提出了多个补丁，解决了 MPAM 的一些具体实现问题，包括对 KVM 的支持、MPAM 寄存器的初始化、以及在 CPU 上线时的上下文切换等。
   - Oliver Upton 对某些补丁提出了建议，建议在文档中明确写入 MPAM1_EL1 的写入后需要进行 ISB（指令同步屏障），以确保上下文同步。
   - 讨论还涉及到对特定硬件缺陷的处理，例如 T241 的一些特定问题，补丁中引入了相应的工作区架构来解决这些问题。

整体来看，本周的讨论和补丁提交进一步推动了 ARM MPAM 与 resctrl 的集成，增强了对虚拟化环境中资源管理的支持。

#### 📝 邮件列表

1. **[12-19 18:11]** [PATCH v2 00/45] arm_mpam: Add KVM/arm64 and resctrl glue code
   - 发件人: Ben Horgan <ben.horgan@arm.com>
2. **[12-19 18:11]** [PATCH v2 01/45] arm_mpam: Stop using uninitialized variables in __ris_msmon_read()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
3. **[12-19 18:11]** [PATCH v2 02/45] arm_mpam: Remove duplicate linux/srcu.h header
   - 发件人: Ben Horgan <ben.horgan@arm.com>
4. **[12-19 18:11]** [PATCH v2 03/45] arm_mpam: Use non-atomic bitops when modifying feature bitmap
   - 发件人: Ben Horgan <ben.horgan@arm.com>
5. **[12-19 18:11]** [PATCH v2 04/45] arm64/sysreg: Add MPAMSM_EL1 register
   - 发件人: Ben Horgan <ben.horgan@arm.com>
6. **[12-19 18:11]** [PATCH v2 05/45] KVM: arm64: Preserve host MPAM configuration when changing traps
   - 发件人: Ben Horgan <ben.horgan@arm.com>
7. **[12-19 18:11]** [PATCH v2 06/45] KVM: arm64: Make MPAMSM_EL1 accesses UNDEF
   - 发件人: Ben Horgan <ben.horgan@arm.com>
8. **[12-19 18:11]** [PATCH v2 07/45] arm64: mpam: Context switch the MPAM registers
   - 发件人: Ben Horgan <ben.horgan@arm.com>
9. **[12-19 18:11]** [PATCH v2 08/45] arm64: mpam: Re-initialise MPAM regs when CPU comes online
   - 发件人: Ben Horgan <ben.horgan@arm.com>
10. **[12-19 18:11]** [PATCH v2 09/45] arm64: mpam: Advertise the CPUs MPAM limits to the driver
   - 发件人: Ben Horgan <ben.horgan@arm.com>
11. **[12-19 18:11]** [PATCH v2 10/45] arm64: mpam: Add cpu_pm notifier to restore MPAM sysregs
   - 发件人: Ben Horgan <ben.horgan@arm.com>
12. **[12-19 18:11]** [PATCH v2 11/45] arm64: mpam: Initialise and context switch the MPAMSM_EL1 register
   - 发件人: Ben Horgan <ben.horgan@arm.com>
13. **[12-19 18:11]** [PATCH v2 12/45] arm64: mpam: Add helpers to change a task or cpu's MPAM PARTID/PMG values
   - 发件人: Ben Horgan <ben.horgan@arm.com>
14. **[12-19 18:11]** [PATCH v2 13/45] KVM: arm64: Force guest EL1 to use user-space's partid configuration
   - 发件人: Ben Horgan <ben.horgan@arm.com>
15. **[12-19 18:11]** [PATCH v2 14/45] KVM: arm64: Use kernel-space partid configuration for hypercalls
   - 发件人: Ben Horgan <ben.horgan@arm.com>
16. **[12-19 18:11]** [PATCH v2 15/45] arm_mpam: resctrl: Add boilerplate cpuhp and domain allocation
   - 发件人: Ben Horgan <ben.horgan@arm.com>
17. **[12-19 18:11]** [PATCH v2 16/45] arm_mpam: resctrl: Sort the order of the domain lists
   - 发件人: Ben Horgan <ben.horgan@arm.com>
18. **[12-19 18:11]** [PATCH v2 17/45] arm_mpam: resctrl: Pick the caches we will use as resctrl resources
   - 发件人: Ben Horgan <ben.horgan@arm.com>
19. **[12-19 18:11]** [PATCH v2 18/45] arm_mpam: resctrl: Implement resctrl_arch_reset_all_ctrls()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
20. **[12-19 18:11]** [PATCH v2 19/45] arm_mpam: resctrl: Add resctrl_arch_get_config()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
21. **[12-19 18:11]** [PATCH v2 20/45] arm_mpam: resctrl: Implement helpers to update configuration
   - 发件人: Ben Horgan <ben.horgan@arm.com>
22. **[12-19 18:11]** [PATCH v2 21/45] arm_mpam: resctrl: Add plumbing against arm64 task and cpu hooks
   - 发件人: Ben Horgan <ben.horgan@arm.com>
23. **[12-19 18:11]** [PATCH v2 22/45] arm_mpam: resctrl: Add CDP emulation
   - 发件人: Ben Horgan <ben.horgan@arm.com>
24. **[12-19 18:11]** [PATCH v2 23/45] arm_mpam: resctrl: Add rmid index helpers
   - 发件人: Ben Horgan <ben.horgan@arm.com>
25. **[12-19 18:11]** [PATCH v2 24/45] arm_mpam: resctrl: Convert to/from MPAMs fixed-point formats
   - 发件人: Ben Horgan <ben.horgan@arm.com>
26. **[12-19 18:11]** [PATCH v2 25/45] arm_mpam: resctrl: Add support for 'MB' resource
   - 发件人: Ben Horgan <ben.horgan@arm.com>
27. **[12-19 18:11]** [PATCH v2 26/45] arm_mpam: resctrl: Add kunit test for control format conversions
   - 发件人: Ben Horgan <ben.horgan@arm.com>
28. **[12-19 18:11]** [PATCH v2 27/45] arm_mpam: resctrl: Add support for csu counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
29. **[12-19 18:11]** [PATCH v2 28/45] arm_mpam: resctrl: Pick classes for use as mbm counters
   - 发件人: Ben Horgan <ben.horgan@arm.com>
30. **[12-19 18:11]** [PATCH v2 29/45] arm_mpam: resctrl: Pre-allocate free running monitors
   - 发件人: Ben Horgan <ben.horgan@arm.com>
31. **[12-19 18:11]** [PATCH v2 30/45] arm_mpam: resctrl: Pre-allocate assignable monitors
   - 发件人: Ben Horgan <ben.horgan@arm.com>
32. **[12-19 18:11]** [PATCH v2 31/45] arm_mpam: resctrl: Add kunit test for ABMC/CDP interactions
   - 发件人: Ben Horgan <ben.horgan@arm.com>
33. **[12-19 18:11]** [PATCH v2 32/45] arm_mpam: resctrl: Add resctrl_arch_config_cntr() for ABMC use
   - 发件人: Ben Horgan <ben.horgan@arm.com>
34. **[12-19 18:11]** [PATCH v2 33/45] arm_mpam: resctrl: Allow resctrl to allocate monitors
   - 发件人: Ben Horgan <ben.horgan@arm.com>
35. **[12-19 18:11]** [PATCH v2 34/45] arm_mpam: resctrl: Add resctrl_arch_rmid_read() and resctrl_arch_reset_rmid()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
36. **[12-19 18:11]** [PATCH v2 35/45] arm_mpam: resctrl: Add resctrl_arch_cntr_read() & resctrl_arch_reset_cntr()
   - 发件人: Ben Horgan <ben.horgan@arm.com>
37. **[12-19 18:11]** [PATCH v2 36/45] arm_mpam: resctrl: Update the rmid reallocation limit
   - 发件人: Ben Horgan <ben.horgan@arm.com>
38. **[12-19 18:11]** [PATCH v2 37/45] arm_mpam: resctrl: Add empty definitions for assorted resctrl functions
   - 发件人: Ben Horgan <ben.horgan@arm.com>
39. **[12-19 18:11]** [PATCH v2 38/45] arm64: mpam: Select ARCH_HAS_CPU_RESCTRL
   - 发件人: Ben Horgan <ben.horgan@arm.com>
40. **[12-19 18:11]** [PATCH v2 39/45] arm_mpam: resctrl: Call resctrl_init() on platforms that can support resctrl
   - 发件人: Ben Horgan <ben.horgan@arm.com>
41. **[12-19 18:11]** [PATCH v2 40/45] arm_mpam: Generate a configuration for min controls
   - 发件人: Ben Horgan <ben.horgan@arm.com>
42. **[12-19 18:11]** [PATCH v2 41/45] arm_mpam: Add quirk framework
   - 发件人: Ben Horgan <ben.horgan@arm.com>
43. **[12-19 18:11]** [PATCH v2 42/45] arm_mpam: Add workaround for T241-MPAM-1
   - 发件人: Ben Horgan <ben.horgan@arm.com>
44. **[12-19 18:11]** [PATCH v2 43/45] arm_mpam: Add workaround for T241-MPAM-4
   - 发件人: Ben Horgan <ben.horgan@arm.com>
45. **[12-19 18:11]** [PATCH v2 44/45] arm_mpam: Add workaround for T241-MPAM-6
   - 发件人: Ben Horgan <ben.horgan@arm.com>
46. **[12-19 18:11]** [PATCH v2 45/45] arm_mpam: Quirk CMN-650's CSU NRDY behaviour
   - 发件人: Ben Horgan <ben.horgan@arm.com>
47. **[12-19 12:01]** Re: [PATCH v2 05/45] KVM: arm64: Preserve host MPAM configuration
 when changing traps
   - 发件人: Oliver Upton <oupton@kernel.org>
48. **[12-19 12:10]** Re: [PATCH v2 13/45] KVM: arm64: Force guest EL1 to use user-space's
 partid configuration
   - 发件人: Oliver Upton <oupton@kernel.org>

---

### Thread 4: [PATCH v2 00/36] KVM: arm64: Introduce vGIC-v5 with PPI support

**📧 邮件数**: 38 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 19 Dec 2025 15:52:35 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（内核虚拟机）在 ARM64 架构下引入虚拟 GICv5（vgic_v5）设备的补丁系列，主要集中在 PPI（私有中断）支持的实现上。

1. **原始补丁内容**：补丁系列的目标是为 KVM 引入 GICv5 设备，初步实现了 PPI 的支持。补丁中包括对 GICv5 特性的检测、PPI 的保存与恢复机制、以及对用户空间可驱动 PPI 的查询接口。

2. **历史讨论要点**：之前的讨论主要集中在 GICv5 的架构特性和与现有 GICv2/GICv3 的兼容性问题。补丁的设计考虑了如何在不暴露未实现的 PPI 的情况下，确保虚拟机的正常运行。

3. **本周新讨论与进展**：本周的讨论中，Sascha Bischoff 提出了多个补丁，涵盖了 GICv5 的初始化、PPI 中断注入、状态同步等功能。特别是，补丁中增加了对 GICv5 的保护模式的隐藏、对用户空间驱动 PPI 的支持，以及对 GICv5 设备的文档说明。此外，还引入了自测代码以验证 GICv5 的功能。最终，Sascha 提到他已将 GICv5 的 kvmtool 支持提交审查。

整体而言，本次补丁系列为 KVM 提供了对 GICv5 的初步支持，增强了虚拟化环境中的中断管理能力。

#### 📝 邮件列表

1. **[12-19 15:52]** [PATCH v2 00/36] KVM: arm64: Introduce vGIC-v5 with PPI support
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[12-19 15:52]** [PATCH v2 02/36] KVM: arm64: gic-v3: Switch vGIC-v3 to use generated
 ICH_VMCR_EL2
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
3. **[12-19 15:52]** [PATCH v2 01/36] KVM: arm64: Account for RES1 bits in
 DECLARE_FEAT_MAP() and co
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
4. **[12-19 15:52]** [PATCH v2 03/36] arm64/sysreg: Drop ICH_HFGRTR_EL2.ICC_HAPR_EL1 and
 make RES1
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
5. **[12-19 15:52]** [PATCH v2 05/36] arm64/sysreg: Add GICR CDNMIA encoding
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
6. **[12-19 15:52]** [PATCH v2 04/36] arm64/sysreg: Add remaining GICv5 ICC_ & ICH_
 sysregs for KVM support
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
7. **[12-19 15:52]** [PATCH v2 06/36] KVM: arm64: gic-v5: Add ARM_VGIC_V5 device to KVM
 headers
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
8. **[12-19 15:52]** [PATCH v2 09/36] KVM: arm64: gic-v5: Detect implemented PPIs on boot
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
9. **[12-19 15:52]** [PATCH v2 07/36] KVM: arm64: gic: Introduce interrupt type helpers
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
10. **[12-19 15:52]** [PATCH v2 08/36] KVM: arm64: Introduce kvm_call_hyp_nvhe_res()
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
11. **[12-19 15:52]** [PATCH v2 12/36] KVM: arm64: gic-v5: Add emulation for
 ICC_IAFFIDR_EL1 accesses
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
12. **[12-19 15:52]** [PATCH v2 11/36] KVM: arm64: gic-v5: Support GICv5 FGTs & FGUs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
13. **[12-19 15:52]** [PATCH v2 10/36] KVM: arm64: gic-v5: Sanitize ID_AA64PFR2_EL1.GCIE
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
14. **[12-19 15:52]** [PATCH v2 14/36] KVM: arm64: gic-v5: Add vgic-v5 save/restore hyp
 interface
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
15. **[12-19 15:52]** [PATCH v2 13/36] KVM: arm64: gic: Set vgic_model before initing
 private IRQs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
16. **[12-19 15:52]** [PATCH v2 16/36] KVM: arm64: gic-v5: Implement direct injection of
 PPIs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
17. **[12-19 15:52]** [PATCH v2 17/36] KVM: arm64: gic: Introduce irq_queue and
 set_pending_state to irq_ops
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
18. **[12-19 15:52]** [PATCH v2 15/36] KVM: arm64: gic-v5: Implement GICv5 load/put and
 save/restore
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
19. **[12-19 15:52]** [PATCH v2 18/36] KVM: arm64: gic-v5: Implement PPI interrupt
 injection
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
20. **[12-19 15:52]** [PATCH v2 20/36] KVM: arm64: gic-v5: Init Private IRQs (PPIs) for
 GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
21. **[12-19 15:52]** [PATCH v2 19/36] KVM: arm64: gic-v5: Check for pending PPIs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
22. **[12-19 15:52]** [PATCH v2 21/36] KVM: arm64: gic-v5: Finalize GICv5 PPIs and generate
 mask
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
23. **[12-19 15:52]** [PATCH v2 23/36] KVM: arm64: gic-v5: Support GICv5 interrupts with
 KVM_IRQ_LINE
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
24. **[12-19 15:52]** [PATCH v2 22/36] KVM: arm64: gic-v5: Trap and mask guest PPI register
 accesses
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
25. **[12-19 15:52]** [PATCH v2 24/36] KVM: arm64: gic-v5: Create, init vgic_v5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
26. **[12-19 15:52]** [PATCH v2 25/36] KVM: arm64: gic-v5: Reset vcpu state
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
27. **[12-19 15:52]** [PATCH v2 26/36] KVM: arm64: gic-v5: Bump arch timer for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
28. **[12-19 15:52]** [PATCH v2 28/36] KVM: arm64: gic: Hide GICv5 for protected guests
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
29. **[12-19 15:52]** [PATCH v2 27/36] KVM: arm64: gic-v5: Mandate architected PPI for PMU
 emulation on GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
30. **[12-19 15:52]** [PATCH v2 31/36] KVM: arm64: gic-v5: Set ICH_VCTLR_EL2.En on boot
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
31. **[12-19 15:52]** [PATCH v2 30/36] KVM: arm64: gic-v5: Introduce kvm_arm_vgic_v5_ops
 and register them
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
32. **[12-19 15:52]** [PATCH v2 29/36] KVM: arm64: gic-v5: Hide FEAT_GCIE from NV GICv5
 guests
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
33. **[12-19 15:52]** [PATCH v2 34/36] Documentation: KVM: Introduce documentation for
 VGICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
34. **[12-19 15:52]** [PATCH v2 33/36] KVM: arm64: gic-v5: Probe for GICv5 device
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
35. **[12-19 15:52]** [PATCH v2 32/36] irqchip/gic-v5: Check if impl is virt capable
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
36. **[12-19 15:52]** [PATCH v2 36/36] KVM: arm64: gic-v5: Communicate userspace-drivable
 PPIs via a UAPI
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
37. **[12-19 15:52]** [PATCH v2 35/36] KVM: arm64: selftests: Introduce a minimal GICv5 PPI
 selftest
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
38. **[12-19 16:17]** Re: [PATCH v2 00/36] KVM: arm64: Introduce vGIC-v5 with PPI support
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>

---

### Thread 5: [PATCH kvmtool 00/17] arm64: Support GICv5-based guests

**📧 邮件数**: 18 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 19 Dec 2025 16:12:53 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的 KVM 工具的 GICv5 支持的补丁系列（共17个补丁）。补丁的主要目标是为基于 GICv5 的虚拟机提供支持，具体包括对 PPIs、SPIs 和 LPIs 的支持。

在历史讨论中，补丁的背景是为了实现 GICv5 的功能，之前的讨论集中在如何实现 GICv5 的基本支持以及与现有 KVM 代码的兼容性。补丁系列中的初始补丁主要实现了对 PPIs 的支持，并计划在后续补丁中添加 IRS 和 ITS 的支持。

本周的新讨论中，Sascha Bischoff 提出了多个补丁，涵盖了 GICv5 的 FDT 节点生成、IRQ 类型更新、以及对 IRS 和 ITS 的支持等。具体进展包括：
1. 添加了 GICv5 的基本支持，允许创建虚拟机并使用 PPIs。
2. 更新了 PMU 和定时器的 FDT 生成代码，以兼容 GICv5。
3. 引入了 GICv5 的 IRS 和 ITS 节点，支持 MSIs。
4. 简化了 GIC 类型检查，增加了对 GICv5 的识别。

整体来看，本周的讨论和补丁推进了 GICv5 的功能实现，使得 KVM 在 ARM64 架构上的虚拟化能力得到了显著增强。

#### 📝 邮件列表

1. **[12-19 16:12]** [PATCH kvmtool 00/17] arm64: Support GICv5-based guests
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[12-19 16:12]** [PATCH 01/17] Sync kernel UAPI headers with v6.19-rc1 with WIP KVM
 GICv5 PPI support
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
3. **[12-19 16:12]** [PATCH 02/17] arm64: Add basic support for creating a VM with GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
4. **[12-19 16:12]** [PATCH 05/17] arm64: Update PMU IRQ/FDT code for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
5. **[12-19 16:12]** [PATCH 03/17] arm64: Introduce GICv5 FDT IRQ types
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
6. **[12-19 16:12]** [PATCH 04/17] arm64: Generate main GICv5 FDT node
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
7. **[12-19 16:12]** [PATCH 07/17] irq: Add interface to override default irq offset
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
8. **[12-19 16:12]** [PATCH 08/17] arm64: Add phandle for CPUs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
9. **[12-19 16:12]** [PATCH 06/17] arm64: Update timer FDT for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
10. **[12-19 16:12]** [PATCH 11/17] arm64: Add GICv5 IRS support
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
11. **[12-19 16:12]** [PATCH 09/17] arm64: Simplify GIC type checks by adding gic__is_v5()
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
12. **[12-19 16:12]** [PATCH 10/17] Sync kernel headers to add WIP GICv5 IRS and ITS
 support in KVM
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
13. **[12-19 16:12]** [PATCH 13/17] arm64: Update generic FDT interrupt desc generator for
 GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
14. **[12-19 16:12]** [PATCH 12/17] arm64: Generate FDT nodes for GICv5's IRS
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
15. **[12-19 16:12]** [PATCH 14/17] arm64: Bump PCI FDT code for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
16. **[12-19 16:12]** [PATCH 17/17] arm64: Update PCI FDT generation for GICv5 ITS MSIs
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
17. **[12-19 16:12]** [PATCH 15/17] arm64: Introduce gicv5-its irqchip
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
18. **[12-19 16:12]** [PATCH 16/17] arm64: Add GICv5 ITS node to FDT
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>

---

### Thread 6: [PATCH v5 00/24] ARM64 PMU Partitioning

**📧 邮件数**: 16 | **👥 参与者**: 2 | **📅 开始时间**: Tue,  9 Dec 2025 20:50:57 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 的性能监控单元（PMU）分区的补丁系列（PATCH v5 00/24）。该补丁旨在创建一种新的 PMU 方案，通过为虚拟机保留一部分计数器，显著降低开销并提高性能。补丁的背景在于 KVM 论坛上对该功能的介绍，包含了性能基准测试的详细信息。

在历史讨论中，主要集中在补丁的不同部分上，包括快速路径 PMU 寄存器处理程序、事件过滤的强制执行以及懒惰的 PMU 上下文切换。参与者 Oliver Upton 提出了多项建议，涉及补丁的设计和实现细节，强调了在处理寄存器时的效率和一致性。

在本周的新讨论中，Oliver 对补丁的具体实现提出了进一步的建议，特别是在处理 PMU 状态和事件过滤方面。他建议在 vcpu_load() 时评估 vPMU 的状态，以确保正确的懒加载机制。此外，Colton Lewis 对 Oliver 的建议表示赞同，并承诺将进行相应的修改。

总体而言，讨论围绕如何优化 ARM64 PMU 的分区和相关实现细节展开，参与者之间的互动推动了补丁的改进和完善。

#### 📝 邮件列表

1. **[12-09 20:50]** [PATCH v5 00/24] ARM64 PMU Partitioning
   - 发件人: Colton Lewis <coltonlewis@google.com>
2. **[12-09 20:51]** [PATCH v5 14/24] KVM: arm64: Write fast path PMU register handlers
   - 发件人: Colton Lewis <coltonlewis@google.com>
3. **[12-09 20:51]** [PATCH v5 18/24] KVM: arm64: Enforce PMU event filter at vcpu_load()
   - 发件人: Colton Lewis <coltonlewis@google.com>
4. **[12-09 13:08]** Re: [PATCH v5 10/24] KVM: arm64: Set up FGT for Partitioned PMU
   - 发件人: Oliver Upton <oupton@kernel.org>
5. **[12-09 14:06]** Re: [PATCH v5 19/24] KVM: arm64: Implement lazy PMU context swaps
   - 发件人: Oliver Upton <oupton@kernel.org>
6. **[12-09 14:52]** Re: [PATCH v5 21/24] KVM: arm64: Inject recorded guest interrupts
   - 发件人: Oliver Upton <oupton@kernel.org>
7. **[12-12 20:51]** Re: [PATCH v5 10/24] KVM: arm64: Set up FGT for Partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
8. **[12-12 22:25]** Re: [PATCH v5 19/24] KVM: arm64: Implement lazy PMU context swaps
   - 发件人: Colton Lewis <coltonlewis@google.com>
9. **[12-12 22:55]** Re: [PATCH v5 21/24] KVM: arm64: Inject recorded guest interrupts
   - 发件人: Colton Lewis <coltonlewis@google.com>
10. **[12-15 09:50]** Re: [PATCH v5 21/24] KVM: arm64: Inject recorded guest interrupts
   - 发件人: Oliver Upton <oupton@kernel.org>
11. **[12-15 10:06]** Re: [PATCH v5 19/24] KVM: arm64: Implement lazy PMU context swaps
   - 发件人: Oliver Upton <oupton@kernel.org>
12. **[12-16 16:13]** Re: [PATCH v5 10/24] KVM: arm64: Set up FGT for Partitioned PMU
   - 发件人: Oliver Upton <oupton@kernel.org>
13. **[12-16 16:38]** Re: [PATCH v5 14/24] KVM: arm64: Write fast path PMU register
 handlers
   - 发件人: Oliver Upton <oupton@kernel.org>
14. **[12-16 16:57]** Re: [PATCH v5 18/24] KVM: arm64: Enforce PMU event filter at
 vcpu_load()
   - 发件人: Oliver Upton <oupton@kernel.org>
15. **[12-17 23:03]** Re: [PATCH v5 14/24] KVM: arm64: Write fast path PMU register handlers
   - 发件人: Colton Lewis <coltonlewis@google.com>
16. **[12-17 23:05]** Re: [PATCH v5 18/24] KVM: arm64: Enforce PMU event filter at vcpu_load()
   - 发件人: Colton Lewis <coltonlewis@google.com>

---

### Thread 7: [PATCH v3 0/4] KVM: arm64: pKVM fixes

**📧 邮件数**: 12 | **👥 参与者**: 4 | **📅 开始时间**: Tue, 16 Dec 2025 10:30:49 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（内核虚拟机）在 arm64 架构下的 pKVM 修复的补丁集（PATCH v3 0/4）。该补丁主要解决了在启用 S1PIE 和 kvm-arm.mode=protected 的情况下，未保护虚拟机（VM）在运行时发生的错误。具体来说，补丁修复了在 VCPU 加载时未能正确传播 FGT（Fault Generation Traps）值的问题，导致了 KVM 触发 BUG_ON 错误。

在历史讨论中，参与者提出了补丁的背景和问题，指出了在运行未保护的 pKVM VCPU 时，未初始化的 FGT 注册值会导致不必要的陷阱和错误访问。补丁集包括四个主要修复：1）在 VCPU 加载时复制 FGT 陷阱；2）为没有访问器的寄存器陷阱注入 UNDEF 异常；3）删除不必要的函数参数；4）移除未使用的参数。

本周的新讨论中，参与者对补丁进行了测试并提供了反馈。Fuad Tabba 和 Marc Zyngier 等人对补丁进行了审核并表示支持，确认其在保护和非保护 VM 上的有效性。整体来看，补丁集得到了积极的响应，参与者们认为这些修复将有助于提升 KVM 的稳定性和可靠性。

#### 📝 邮件列表

1. **[12-16 10:30]** [PATCH v3 0/4] KVM: arm64: pKVM fixes
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[12-16 10:30]** [PATCH v3 1/4] KVM: arm64: Copy FGT traps to unprotected pKVM VCPU on VCPU load
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
3. **[12-16 10:30]** [PATCH v3 2/4] KVM: arm64: Inject UNDEF for a register trap without accessor
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
4. **[12-16 10:30]** [PATCH v3 3/4] KVM: arm64: Remove extra argument for __pvkm_host_{share,unshare}_hyp()
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
5. **[12-16 10:30]** [PATCH v3 4/4] KVM: arm64: Remove unused parameter in synchronize_vcpu_pstate()
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
6. **[12-16 10:43]** Re: [PATCH v3 0/4] KVM: arm64: pKVM fixes
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[12-17 09:18]** Re: [PATCH v3 0/4] KVM: arm64: pKVM fixes
   - 发件人: Marc Zyngier <maz@kernel.org>
8. **[12-19 19:28]** [PATCH v3 0/4] KVM: selftests: arm64: Improve diagnostics from
 set_id_regs
   - 发件人: Mark Brown <broonie@kernel.org>
9. **[12-19 19:28]** [PATCH v3 1/4] KVM: selftests: arm64: Report set_id_reg reads of
 test registers as tests
   - 发件人: Mark Brown <broonie@kernel.org>
10. **[12-19 19:28]** [PATCH v3 2/4] KVM: selftests: arm64: Report register reset tests
 individually
   - 发件人: Mark Brown <broonie@kernel.org>
11. **[12-19 19:28]** [PATCH v3 3/4] KVM: selftests: arm64: Make set_id_regs bitfield
 validatity checks non-fatal
   - 发件人: Mark Brown <broonie@kernel.org>
12. **[12-19 19:28]** [PATCH v3 4/4] KVM: selftests: arm64: Skip all 32 bit IDs when
 set_id_regs is aarch64 only
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 8: [PATCH v2 0/4] KVM: arm64: pKVM fixes

**📧 邮件数**: 10 | **👥 参与者**: 3 | **📅 开始时间**: Mon, 15 Dec 2025 11:44:05 +0000

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 pKVM 修复，包含四个补丁（patch）。补丁的主要内容如下：

1. **原始补丁/问题**：补丁旨在解决在启用 S1PIE 和 kvm-arm.mode=protected 的情况下，运行未保护的虚拟机时出现的 BUG。具体问题是，未能正确传播 FGT（Fault Generation Traps）值，导致访问 PIRE0_EL1 时触发错误。

2. **之前讨论要点**：在 v1 版本中，开发者指出了未保护 pKVM VCPU 的 FGT 配置问题，并提出了打印寄存器编码的建议，以便更好地调试此类错误。补丁 v2 版本在此基础上进行了重构和改进。

3. **本周的新讨论、进展或结论**：本周的讨论集中在对补丁的细节审查和改进建议上。参与者 Fuad Tabba 和 Marc Zyngier 对补丁进行了审查并提出了建议，如在寄存器访问时引入更一致的错误处理方式。Alexandru Elisei 也回应了这些建议，表示将考虑在未来的补丁中进行调整。整体来看，补丁得到了积极的反馈，并且讨论推动了对 KVM 错误处理机制的一致性改进。

#### 📝 邮件列表

1. **[12-15 11:44]** [PATCH v2 0/4] KVM: arm64: pKVM fixes
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[12-15 11:44]** [PATCH v2 1/4] KVM: arm64: Copy FGT traps to unprotected pKVM VCPU on VCPU load
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
3. **[12-15 11:44]** [PATCH v2 2/4] KVM: arm64: Print register encoding if there's no accessor
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
4. **[12-15 11:44]** [PATCH v2 3/4] KVM: arm64: Remove extra argument for __pvkm_host_{share,unshare}_hyp()
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
5. **[12-15 11:44]** [PATCH v2 4/4] KVM: arm64: Remove unused parameter in synchronize_vcpu_pstate()
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
6. **[12-15 13:42]** Re: [PATCH v2 4/4] KVM: arm64: Remove unused parameter in synchronize_vcpu_pstate()
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[12-15 13:43]** Re: [PATCH v2 3/4] KVM: arm64: Remove extra argument for __pvkm_host_{share,unshare}_hyp()
   - 发件人: Fuad Tabba <tabba@google.com>
8. **[12-15 13:58]** Re: [PATCH v2 2/4] KVM: arm64: Print register encoding if there's no accessor
   - 发件人: Marc Zyngier <maz@kernel.org>
9. **[12-15 15:17]** Re: [PATCH v2 2/4] KVM: arm64: Print register encoding if there's no
 accessor
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
10. **[12-15 15:39]** Re: [PATCH v2 2/4] KVM: arm64: Print register encoding if there's no accessor
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 9: [PATCH v5 04/27] iommu/io-pgtable-arm: Factor kernel specific
 code out

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 12 Dec 2025 15:37:43 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM 架构的 IOMMU 和页表管理的补丁（PATCH v5 04/27），其目的是将与内核特定相关的代码进行分离，以提高代码的可重用性和模块化。

在历史讨论中，参与者主要探讨了补丁的实现细节，包括如何处理 DMA 映射和内存分配等问题。Jason Gunthorpe 提到，当前的实现依赖于 DMA API，可能在未来的补丁系列中遇到问题，因此需要考虑更改。Mostafa Saleh 也表示，代码的重用性很高，转换为通用页表时应能顺利适配到虚拟化环境中。

在本周的新讨论中，Mostafa 提出希望直接用架构缓存刷新调用替代 dma_map/unmap，以避免未来可能出现的模块化问题。Jason 进一步分析了 CMO（缓存管理操作）未对模块导出的原因，并表示将对此进行清理。此外，关于其他补丁（如 IDR 解析和 KVM 设备探测）的讨论也在进行中，Jason 强调了内核的单体结构，认为不必担心模块间的复杂交互。

总体来看，本周的讨论集中在补丁的实现细节和未来的改进方向上，参与者们积极交流，推动了补丁的进展。

#### 📝 邮件列表

1. **[12-12 15:37]** Re: [PATCH v5 04/27] iommu/io-pgtable-arm: Factor kernel specific
 code out
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[12-12 15:42]** Re: [PATCH v5 07/27] iommu/arm-smmu-v3: Move IDR parsing to common
 functions
   - 发件人: Mostafa Saleh <smostafa@google.com>
3. **[12-12 15:53]** Re: [PATCH v5 14/27] iommu/arm-smmu-v3: Support probing KVM emulated
 devices
   - 发件人: Mostafa Saleh <smostafa@google.com>
4. **[12-15 20:58]** Re: [PATCH v5 04/27] iommu/io-pgtable-arm: Factor kernel specific
 code out
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
5. **[12-16 23:08]** Re: [PATCH v5 04/27] iommu/io-pgtable-arm: Factor kernel specific
 code out
   - 发件人: Mostafa Saleh <smostafa@google.com>
6. **[12-17 09:59]** Re: [PATCH v5 07/27] iommu/arm-smmu-v3: Move IDR parsing to common
 functions
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>
7. **[12-17 10:00]** Re: [PATCH v5 14/27] iommu/arm-smmu-v3: Support probing KVM emulated
 devices
   - 发件人: Jason Gunthorpe <jgg@ziepe.ca>

---

### Thread 10: [PATCH v2 0/5] KVM: selftests: Alignment fixes and arm64 MMU cleanup

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 15 Dec 2025 16:51:50 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 自测的补丁系列，主要集中在内存对齐修复和 arm64 MMU 清理。

1. **原始补丁内容**：本次补丁系列（PATCH v2 0/5）旨在修复 KVM 自测中的内存对齐问题，增强 arm64 MMU 配置，并修复一些文档中的小错误。补丁包括禁用未使用的 TTBR1_EL1 转换、修正 `page_align()` 的实现、将 `page_align()` 移动到共享头文件，以及更新一些注释和参数描述。

2. **之前讨论要点**：在之前的讨论中，开发者们关注了 KVM 自测中的内存管理问题，特别是如何确保在不同架构下的内存对齐和 MMU 配置的正确性。虽然没有详细的历史邮件记录，但可以推测出这些问题的复杂性和重要性。

3. **本周新讨论和进展**：本周的讨论主要由 Fuad Tabba 提供，详细介绍了每个补丁的具体内容和目的。补丁中修复了 arm64 和 riscv 的 `page_align()` 函数的错误，确保其正确处理已对齐的地址，避免内存浪费。此外，补丁还将 `page_align()` 函数移动到共享的 `kvm_util.h` 头文件中，以减少代码重复。最后，修复了一些文档中的错误，确保描述与实际代码一致。

整体来看，本周的讨论集中在对 KVM 自测代码的清理和优化上，旨在提高代码的可维护性和可靠性。

#### 📝 邮件列表

1. **[12-15 16:51]** [PATCH v2 0/5] KVM: selftests: Alignment fixes and arm64 MMU cleanup
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[12-15 16:51]** [PATCH v2 1/5] KVM: arm64: selftests: Disable unused TTBR1_EL1 translations
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[12-15 16:51]** [PATCH v2 2/5] KVM: arm64: selftests: Fix incorrect rounding in page_align()
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[12-15 16:51]** [PATCH v2 3/5] KVM: riscv: selftests: Fix incorrect rounding in page_align()
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[12-15 16:51]** [PATCH v2 4/5] KVM: selftests: Move page_align() to shared header
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[12-15 16:51]** [PATCH v2 5/5] KVM: selftests: Fix typos and stale comments in kvm_util
   - 发件人: Fuad Tabba <tabba@google.com>
7. **[12-17 21:39]** Re: [PATCH v2 4/5] KVM: arm64: Enable HDBSS support and handle HDBSSF
 events
   - 发件人: Robert Hoo <robert.hoo.linux@gmail.com>

---

### Thread 11: [PATCH v1 0/5] KVM: selftests: Alignment fixes and arm64 MMU cleanup

**📧 邮件数**: 6 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 15 Dec 2025 15:45:28 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM 自测的补丁系列，主要集中在对 arm64 MMU 配置的清理和内存对齐问题的修复。

1. **原始补丁内容**：该补丁系列（共五个补丁）旨在修复 KVM 自测中的内存对齐错误，增强 arm64 MMU 配置，并修正一些文档问题。补丁包括禁用未使用的 TTBR1 地址范围的翻译表查找、修复 `page_align()` 函数的实现、将该函数移动到共享头文件以消除代码重复，以及更新文档中的描述。

2. **之前讨论要点**：在此之前并没有相关的历史讨论，所有内容均为本周新讨论的补丁。

3. **本周新讨论与进展**：本周的讨论主要围绕每个补丁的具体实现细节。Fuad Tabba 提出了补丁，详细说明了如何禁用 TTBR1 的翻译表查找，以避免未初始化的寄存器导致不可预测的行为。同时，修复了 `page_align()` 函数在处理已对齐地址时的错误逻辑，确保不会浪费内存。补丁还包括将 `page_align()` 移动到共享头文件和修正文档中的小错误。所有补丁已基于 Linux 6.19-rc1 进行开发，确保了与当前内核版本的兼容性。

总体来看，本周的讨论集中在提升 KVM 自测的稳定性和准确性上，确保在不同架构下的内存管理更加可靠。

#### 📝 邮件列表

1. **[12-15 15:45]** [PATCH v1 0/5] KVM: selftests: Alignment fixes and arm64 MMU cleanup
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[12-15 15:45]** [PATCH v1 1/5] KVM: arm64: selftests: Disable unused TTBR1_EL1 translations
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[12-15 15:45]** [PATCH v1 2/5] KVM: arm64: selftests: Fix incorrect rounding in page_align()
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[12-15 15:45]** [PATCH v1 3/5] KVM: riscv: selftests: Fix incorrect rounding in page_align()
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[12-15 15:45]** [PATCH v1 4/5] KVM: selftests: Move page_align() to shared header
   - 发件人: Fuad Tabba <tabba@google.com>
6. **[12-15 15:45]** [PATCH v1 5/5] KVM: selftests: Fix typos and stale comments in kvm_util
   - 发件人: Fuad Tabba <tabba@google.com>

---

### Thread 12: [PATCH v2 0/6] KVM: arm64: VTCR_EL2 conversion to feature dependency framework

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 10 Dec 2025 17:30:18 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 VTCR_EL2 转换为特性依赖框架的补丁系列。历史讨论中，Marc Zyngier 提出了一个补丁系列（PATCH v2 0/6），旨在修复与 FEAT_XNX 相关的问题，并扩展了 DECLARE_FEAT_MAP() 中 RES1 处理的范围，以适应即将到来的 GICv5 质量改进。此外，他还简化了 S2TGRANx 的检测。

在本周的新讨论中，Leonardo Bras 对 Marc 提出的补丁（PATCH v2 1/6）进行了回应，询问该补丁是否符合 Arm ARM 文档中的相关描述。Marc 随后补充说明，提到在 M.a.a 中，这些内容属于 I_GLMLD，并指出 R_JJNHR 是一个更有趣的信息来源，详细描述了 XN、UXN 和 PXN 在特定条件下如何共享相同的两个位。

总体来看，本周的讨论主要集中在对补丁的技术细节和标准文档的对照上，参与者们对补丁的适用性和准确性进行了深入探讨。

#### 📝 邮件列表

1. **[12-10 17:30]** [PATCH v2 0/6] KVM: arm64: VTCR_EL2 conversion to feature dependency framework
   - 发件人: Marc Zyngier <maz@kernel.org>
2. **[12-10 17:30]** [PATCH v2 1/6] KVM: arm64: Fix EL2 S1 XN handling for hVHE setups
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[12-19 13:38]** Re: [PATCH v2 1/6] KVM: arm64: Fix EL2 S1 XN handling for hVHE setups
   - 发件人: Leonardo Bras <leo.bras@arm.com>
4. **[12-19 14:13]** Re: [PATCH v2 1/6] KVM: arm64: Fix EL2 S1 XN handling for hVHE setups
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 13: [PATCH v4 0/2] arm: add kvm-psci-version vcpu property

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Tue,  2 Dec 2025 17:08:51 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 ARM 架构的 KVM（Kernel-based Virtual Machine）补丁系列，主要是添加一个 vcpu 属性以支持特定的 PSCI（Power State Coordination Interface）版本。该补丁的目的是为了在主机内核的默认 PSCI 版本不同的情况下，支持虚拟机的迁移。

在历史讨论中，Sebastian Ott 提出了两个补丁：第一个补丁添加了一个 vcpu 属性，允许通过 KVM_REG_ARM_PSCI_VERSION FW 寄存器请求特定的 PSCI 版本；第二个补丁则为新的 PSCI 版本（1_2 和 1_3）添加了常量。这些补丁旨在解决在不同 PSCI 版本之间的兼容性问题。

在本周的新讨论中，Stefan Weil 对第一个补丁进行了审核并表示通过。Sebastian Ott 随后询问是否还有其他需要处理的事项，以便将补丁合并。这表明该补丁系列正在接近合并阶段，参与者们对其进展持积极态度。

#### 📝 邮件列表

1. **[12-02 17:08]** [PATCH v4 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[12-02 17:08]** [PATCH v4 1/2] target/arm/kvm: add constants for new PSCI versions
   - 发件人: Sebastian Ott <sebott@redhat.com>
3. **[12-18 08:56]** Re: [PATCH v4 1/2] target/arm/kvm: add constants for new PSCI
 versions
   - 发件人: Stefan Weil <sw@weilnetz.de>
4. **[12-18 11:47]** Re: [PATCH v4 0/2] arm: add kvm-psci-version vcpu property
   - 发件人: Sebastian Ott <sebott@redhat.com>

---

### Thread 14: [PATCH v11 RESEND 0/9] support FEAT_LSUI

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Sun, 14 Dec 2025 11:22:39 +0000

#### 🤖 AI 总结

本邮件线程讨论了支持 Arm 架构中的 FEAT_LSUI 特性的补丁集，主要涉及如何在不清除 PSTATE.PAN 位的情况下，通过加载/存储指令访问用户内存。Yeoreum Yun 提出的补丁集（PATCH v11 RESEND 0/9）旨在优化 futex 原子操作和用户 swpX 模拟，替换掉需要清除 PSTATE.PAN 位的 ldxr/st{l}xr 指令。

在历史讨论中，Yeoreum 详细阐述了补丁的目的和实现，特别是补丁 9/9 针对过时的 swpX 指令的模拟，强调了使用 FEAT_LSUI 指令的重要性，以避免在使用相关指令时切换 PSTATE.PAN 位。

在本周的新讨论中，Marc Zyngier 提出了对未来 CPU 同时实现 LSUI 和 AArch32 的可能性的质疑，认为这种情况极不可能。Yeoreum 对此表示不确定，并提到目前大多数 CPU 的 ID_AA64PFR0_EL1.EL0 位设置为 0b0010。他对是否保留与过时 swp 指令相关的补丁（第 8 和 9 个补丁）持开放态度，希望将此决定留给维护者。整体来看，讨论围绕补丁的有效性和未来 CPU 兼容性展开，尚未达成明确结论。

#### 📝 邮件列表

1. **[12-14 11:22]** [PATCH v11 RESEND 0/9] support FEAT_LSUI
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
2. **[12-14 11:22]** [PATCH v11 RESEND 9/9] arm64: armv8_deprecated: apply FEAT_LSUI for swpX emulation.
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>
3. **[12-15 09:33]** Re: [PATCH v11 RESEND 9/9] arm64: armv8_deprecated: apply FEAT_LSUI for swpX emulation.
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[12-15 09:56]** Re: [PATCH v11 RESEND 9/9] arm64: armv8_deprecated: apply FEAT_LSUI
 for swpX emulation.
   - 发件人: Yeoreum Yun <yeoreum.yun@arm.com>

---

### Thread 15: [PATCH v6 00/44] KVM: x86: Add support for mediated vPMUs

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Fri,  5 Dec 2025 16:16:36 -0800

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM (Kernel-based Virtual Machine) 的一个补丁系列，主要目的是为 x86 架构添加对中介虚拟性能监控单元（mediated vPMUs）的支持。补丁系列的提交者是 Sean Christopherson，邮件中提到该补丁基于 KVM 6.19 的 pull 请求，并计划将其合并到相应的代码树中。

在历史讨论中，Peter Zijlstra 对补丁的整体状态表示认可，并提出了一些小的修改建议，认为可以在合并后进行调整。他计划在 KVM 6.19 的 rc1 发布后将这些补丁排入队列。

在本周的新讨论中，Manali Shukla 报告了对该补丁系列的测试结果。她在 AMD EPYC 9745 处理器上进行了长达 12 小时的性能测试，测试了多种配置，结果显示没有出现新的故障。所有 KVM 单元测试（KUT）在不同配置组合下均通过，表明补丁在实际应用中表现良好。

总体来看，该补丁系列在历史讨论中获得了积极反馈，并在本周的测试中也显示出稳定性和可靠性，为其合并奠定了良好的基础。

#### 📝 邮件列表

1. **[12-05 16:16]** [PATCH v6 00/44] KVM: x86: Add support for mediated vPMUs
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[12-08 16:37]** Re: [PATCH v6 00/44] KVM: x86: Add support for mediated vPMUs
   - 发件人: Peter Zijlstra <peterz@infradead.org>
3. **[12-18 14:49]** Re: [PATCH v6 00/44] KVM: x86: Add support for mediated vPMUs
   - 发件人: Manali Shukla <manali.shukla@amd.com>

---

### Thread 16: [PATCH v3 1/3] KVM: arm64: Add pre_fault_memory implementation

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 15 Dec 2025 11:43:06 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下实现 pre_fault_memory 的补丁（patch）。该补丁旨在优化内存故障处理，以提升虚拟化性能。

在历史讨论中，并没有提供详细的背景信息或先前的讨论内容，因此我们无法获取补丁的具体细节或之前的讨论要点。

在本周的新讨论中，参与者 Marc Zyngier 针对 pKVM（保护虚拟机）场景提出了一个问题，询问在处理此类情况时是否应该返回 -EPERM 错误码。他提到已经找到一个补丁系列，似乎可以解决这个问题，并询问是否希望将其纳入当前的补丁系列中。这表明在补丁的实现过程中，针对特定场景的安全性和错误处理机制仍需进一步讨论和完善。

总体来看，本周的讨论集中在如何处理 pKVM 情境下的内存故障问题上，显示出对补丁的进一步审查和改进的需求。

#### 📝 邮件列表

1. **[12-15 11:43]** Re: [PATCH v3 1/3] KVM: arm64: Add pre_fault_memory implementation
   - 发件人: Thomson, Jack <jackabt.amazon@gmail.com>

---

## 📌 RFC

共 6 个 thread

---

### Thread 1: [RFC PATCH v6 05/35] KVM: arm64: Add KVM_CAP_ARM_SPE capability

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Sun, 14 Dec 2025 20:18:42 +0800

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（内核虚拟机）在 arm64 架构中添加 KVM_CAP_ARM_SPE 功能的补丁（patch）。该补丁旨在增强 KVM 的性能和功能，特别是在处理 ARM 体系结构的 SPE（可扩展性能监控）时。

在历史讨论中，参与者 Leo Yan 提出了一个建议，即可以通过检查 `list_empty(&arm_spus)` 来简化 `kvm_supports_spe()` 函数的实现，从而不再需要静态键 `kvm_spe_available`。他指出，这样的改动不仅简化了代码，还与 CPU PMU（性能监控单元）的虚拟化实现保持一致。

在本周的新讨论中，Alexandru Elisei 对 Leo 的建议表示赞同，并承认自己在补丁中添加静态键是出于对性能的考虑，但在审视整个补丁系列后，他意识到并未实际使用该静态键。此讨论表明，开发者们在优化代码和性能方面保持开放的态度，并愿意根据反馈进行调整。

总体来看，邮件讨论集中在如何优化 KVM 的实现，以提高其在 ARM 架构下的性能和一致性。

#### 📝 邮件列表

1. **[12-14 20:18]** Re: [RFC PATCH v6 05/35] KVM: arm64: Add KVM_CAP_ARM_SPE capability
   - 发件人: Leo Yan <leo.yan@linux.dev>
2. **[12-15 11:46]** Re: [RFC PATCH v6 05/35] KVM: arm64: Add KVM_CAP_ARM_SPE capability
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

### Thread 2: [RFC PATCH v6 17/35] KVM: arm64: Add writable SPE system
 registers to VCPU context

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 16 Dec 2025 11:54:54 +0000

#### 🤖 AI 总结

本邮件主题为“[RFC PATCH v6 17/35] KVM: arm64: Add writable SPE system registers to VCPU context”，主要讨论在 KVM 的 arm64 架构中为 VCPU 上下文添加可写的 SPE 系统寄存器。

在本周的新讨论中，参与者 Suzuki K Poulose 对之前的讨论进行了回复，指出 Alexandru Elisei 提到的 MDCR_EL2_E2TB_MASK 是用于跟踪缓冲区的。这一细节的澄清表明，参与者们在关注寄存器的具体功能和用途，确保对补丁的理解准确。

由于本邮件线程没有历史讨论的部分，无法提供之前的讨论要点。总体来看，本周的讨论集中在对补丁中寄存器功能的细致审查上，反映出参与者对技术细节的重视。

#### 📝 邮件列表

1. **[12-16 11:54]** Re: [RFC PATCH v6 17/35] KVM: arm64: Add writable SPE system
 registers to VCPU context
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>

---

### Thread 3: [RFC PATCH v6 16/35] KVM: arm64: Advertise SPE version in
 ID_AA64DFR0_EL1.PMSver

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 16 Dec 2025 11:40:20 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM 在 arm64 架构中如何在 ID_AA64DFR0_EL1.PMSver 中宣传 SPE 版本的补丁（RFC PATCH v6 16/35）。该补丁的目的是在系统中正确反映当前 CPU 的 SPE 版本。

在历史讨论中，尚未有相关的邮件记录，因此没有提供背景信息。

在本周的新讨论中，参与者 Suzuki K Poulose 对补丁提出了几个关键问题。他指出，当前的代码实现与预期不符，具体来说，`read_sanitised_ftr_reg()` 函数返回的是系统范围内的标准化版本，而不是当前 CPU 的版本。他建议使用 `read_sysreg_s()` 来获取正确的 CPU 版本。此外，Suzuki 还提到 PMSVer 已经被标记为 FTR_LOWER_SAFE，因此不需要在此处进行覆盖。他进一步询问，是否应该忽略用户设置的值，而是使用已选择的 SPE 实例，并建议考虑将其设为不可写。

总结来看，本周的讨论集中在补丁的实现细节和潜在的设计选择上，尚未达成最终结论。

#### 📝 邮件列表

1. **[12-16 11:40]** Re: [RFC PATCH v6 16/35] KVM: arm64: Advertise SPE version in
 ID_AA64DFR0_EL1.PMSver
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>

---

### Thread 4: [RFC PATCH v6 01/35] arm64/sysreg: Add new SPE fields

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 15 Dec 2025 21:42:33 +0000

#### 🤖 AI 总结

本邮件主题为“[RFC PATCH v6 01/35] arm64/sysreg: Add new SPE fields”，涉及对 ARM64 架构中系统寄存器（sysreg）添加新的 SPE（可扩展性能监控）字段的补丁。邮件中只有一条新的讨论，未涉及历史讨论。

在本周的新讨论中，参与者 Suzuki K Poulose 对补丁中的定义表示认可，认为其正确。同时，他指出了一个小的格式问题，涉及到 PMBIDR_EL1 的标记。此次讨论没有提出新的问题或异议，主要集中在对补丁内容的确认和细节的微调。

总结而言，本周的讨论主要是对补丁内容的确认，未见显著的争议或进一步的修改建议。

#### 📝 邮件列表

1. **[12-15 21:42]** Re: [RFC PATCH v6 01/35] arm64/sysreg: Add new SPE fields
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>

---

### Thread 5: [RFC PATCH v6 02/35] arm64/sysreg: Define MDCR_EL2.E2PB values

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 15 Dec 2025 21:33:34 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于一个针对 ARM64 架构的补丁（patch），具体内容是定义 MDCR_EL2.E2PB 的值。该补丁是 RFC（请求反馈）版本的第六轮，编号为 02/35。

在历史讨论中，邮件列表中没有提供详细的背景信息，因此无法总结之前的讨论要点。

在本周的新讨论中，Suzuki K Poulose 对该补丁进行了审查，并表示已审核通过（Reviewed-by）。这表明补丁在技术上得到了认可，可能会进入进一步的开发或合并阶段。

总的来说，本周的进展主要是补丁获得了审查通过的反馈，显示出该补丁在社区中的接受度。

#### 📝 邮件列表

1. **[12-15 21:33]** Re: [RFC PATCH v6 02/35] arm64/sysreg: Define MDCR_EL2.E2PB values
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>

---

### Thread 6: [RFC PATCH v6 08/35] HACK! KVM: arm64: Enable SPE virtualization
 only in VHE mode

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 15 Dec 2025 17:49:01 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 VHE 模式下启用 KVM 的 SPE 虚拟化的补丁（RFC PATCH v6 08/35）。该补丁旨在优化 ARM64 架构下的虚拟化性能，特别是在 VHE（Virtualization Host Extensions）模式中。

在之前的讨论中，参与者们一致认为应优先关注 VHE 模式的实现，但也提到需要考虑如何在不同的虚拟化模式之间统一解决方案。讨论中指出，除了寄存器访问和中断处理外，缓冲区管理是该系列补丁中最复杂的部分，因此了解这些更改是否能支持其他模式显得尤为重要。

在本周的新讨论中，Leo Yan 对补丁表示支持，并强调了缓冲区管理的复杂性。他提出了一个有趣的问题，即是否可以重用 virtio-iommu 或 DMA 缓冲区分配来支持 SPE。他认为，IOMMU 的情况可能更简单，因为页表的分配和映射完全发生在主机端。

综上所述，本周的讨论进一步深化了对补丁的理解，并提出了潜在的改进方向，尤其是在缓冲区管理和不同虚拟化模式的统一性方面。

#### 📝 邮件列表

1. **[12-15 17:49]** Re: [RFC PATCH v6 08/35] HACK! KVM: arm64: Enable SPE virtualization
 only in VHE mode
   - 发件人: Leo Yan <leo.yan@arm.com>

---

## 📌 Bug Report

共 2 个 thread

---

### Thread 1: sea_to_user sefltest failure

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 11 Dec 2025 19:11:35 +0100 (CET)

#### 🤖 AI 总结

在本次邮件讨论中，主题为“sea_to_user 自测失败”的问题引起了参与者的关注。历史讨论中，Jiaqi Yan 提到在进行测试时，测试被跳过，可能是因为 EINJ 模块未加载，导致无法正确执行相关操作。具体的测试步骤和输出结果显示了内存映射和数据状态，但最终未能成功完成测试。

在本周的新讨论中，Gavin Shan 进一步分析了问题，指出背后的内存与 1GB 的 hugetlb 页面相关，而在 64KB 主机上可能需要使用 512MB 的 hugetlb 页面。Gavin 还分享了他在 4KB 主机上成功运行测试的经验，详细列出了测试步骤和输出，表明在适当的内存配置下，测试可以正常通过。

综上所述，当前讨论集中在如何调整内存页面大小以解决测试失败的问题，并且在不同主机配置下的测试结果显示出明显差异。

#### 📝 邮件列表

1. **[12-11 19:11]** Re: sea_to_user sefltest failure
   - 发件人: Sebastian Ott <sebott@redhat.com>
2. **[12-15 15:54]** Re: sea_to_user sefltest failure
   - 发件人: Gavin Shan <gshan@redhat.com>

---

### Thread 2: sea_to_user sefltest failure

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 11 Dec 2025 18:54:25 +0100 (CET)

#### 🤖 AI 总结

本邮件讨论的主题是关于 `sea_to_user` 测试失败的问题。历史讨论中，Sebastian Ott 提出了在运行 `sea_to_user` 测试时遇到的错误，具体表现为内存分配失败，导致测试断言失败。错误信息显示在 `kvm_syscalls.h` 的第58行，提示无法分配内存（errno=12）。

在之前的讨论中，虽然没有提供更多的背景信息，但可以推测这个问题可能与内存管理或资源分配有关，尤其是在虚拟化环境下的 KVM（Kernel-based Virtual Machine）相关功能。

本周没有新的讨论或进展更新，邮件列表中没有新的回复或解决方案。因此，当前问题仍然悬而未决，参与者可能需要进一步的调试或提供更多的上下文信息，以便找到解决方案。

#### 📝 邮件列表

1. **[12-11 18:54]** sea_to_user sefltest failure
   - 发件人: Sebastian Ott <sebott@redhat.com>

---

## 📌 Discussion

共 1 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf functions

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 17 Dec 2025 17:44:43 -0800

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM 单元测试的补丁（PATCH v2 0/4），旨在改善叶子函数的回溯信息。

**原始补丁内容**：该补丁主要集中在优化 KVM 测试中的回溯功能，以便更好地追踪叶子函数的执行情况。

**之前的讨论要点**：在历史讨论中，参与者们探讨了如何处理寄存器的共享问题，Sean Christopherson 提到在实现过程中遇到了寄存器损坏和同步问题，尤其是在多核环境下的测试失败。这些问题导致了对测试逻辑的反复修改和调试。

**本周的新讨论与进展**：本周的讨论中，Sean 和 Mathias 继续深入探讨了寄存器的每 CPU 处理方式，并提出了通过使用 MSR_KVM_WALL_CLOCK_NEW 来解决同步问题的方案。Sean 通过代码修改成功解决了部分测试失败的问题，并计划发布新的补丁系列。Mathias 对 Sean 的工作表示感谢，并提到他在假期期间可能无法立即提供反馈。此外，Mathias 还提到已修复的 GCC 错误，建议在补丁中注明相关信息。

总体来看，本周的讨论推动了补丁的进展，并解决了一些关键的同步问题，为后续的测试和开发奠定了基础。

#### 📝 邮件列表

1. **[12-17 17:44]** Re: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf functions
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[12-18 11:07]** Re: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf
 functions
   - 发件人: Mathias Krause <minipli@grsecurity.net>
3. **[12-18 10:26]** Re: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf functions
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[12-19 14:19]** Re: [kvm-unit-tests PATCH v2 0/4] Better backtraces for leaf
 functions
   - 发件人: Mathias Krause <minipli@grsecurity.net>

---

## 📌 Other

共 1 个 thread

---

### Thread 1: hello

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 18 Dec 2025 13:31:33 -0600

#### 🤖 AI 总结

本周的邮件讨论中，参与者TotallyMonke表示他正在查看这个邮件列表，因为他对ARM架构感兴趣，并且听说这个列表与ARM相关。然而，邮件中并没有提及具体的补丁或问题，也没有历史讨论的上下文。因此，目前的讨论内容较为简单，主要是对邮件列表的关注和探索，并未涉及具体的技术问题或进展。整体来看，本周的讨论缺乏实质性的技术交流。

#### 📝 邮件列表

1. **[12-18 13:31]** hello
   - 发件人: TotallyMonke <trontanner@gmail.com>

---

