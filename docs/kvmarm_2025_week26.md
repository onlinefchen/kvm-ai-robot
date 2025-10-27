# KVMARM 邮件列表 AI 总结报告

**生成时间**: 2025-10-27 11:08:40

**分析周期**: 最近 7 天

## 📊 总体统计

- **总邮件数**: 284
- **总 Thread 数**: 36
- **大型 Thread** (>20封): 4 个

### 分类分布

- **PATCH**: 28 threads (245 邮件)
- **RFC**: 3 threads (8 邮件)
- **Selftest**: 1 threads (1 邮件)
- **GIT PULL**: 1 threads (1 邮件)
- **Other**: 3 threads (29 邮件)

---

## 📌 PATCH

共 28 个 thread

---

### Thread 1: [PATCH v3 00/22] ARM64 PMU Partitioning

**📧 邮件数**: 33 | **👥 参与者**: 4 | **📅 开始时间**: Thu, 26 Jun 2025 20:04:36 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 ARM64 架构的 PMU（性能监控单元）分区的补丁系列（PATCH v3 00/22）。该补丁旨在通过允许将 PMU 计数器分为主机和客户机的可访问区域，从而减少开销并提高性能。

**原始补丁/问题内容**：
补丁系列的核心是实现 PMU 的分区，允许主机保留部分计数器供客户机直接访问。补丁中引入了一个模块参数 `reserved_host_counters`，用于在启动时设置保留给主机的计数器数量。

**之前讨论要点**：
历史讨论中，补丁的设计考虑了 PMU 的分区对性能的影响，并提出了在 VHE 模式下支持此功能的必要性。参与者们讨论了分区的实现细节，包括如何处理 PMU 计数器的访问和中断。

**本周的新讨论、进展或结论**：
本周的讨论集中在补丁的具体实现上，包括对 PMU 相关寄存器的处理、如何在分区模式下有效管理中断、以及如何确保客户机和主机之间的隔离。补丁中还增加了对 PMU 事件过滤的支持，确保只有未被过滤的事件计数。此外，讨论中提到了一些代码的清理和重构，以提高可读性和维护性。最终，补丁系列的测试用例也被更新，以确保新功能的正确性和稳定性。

#### 📝 邮件列表

1. **[06-26 20:04]** [PATCH v3 00/22] ARM64 PMU Partitioning
   - 发件人: Colton Lewis <coltonlewis@google.com>
2. **[06-26 20:04]** [PATCH v3 01/22] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Colton Lewis <coltonlewis@google.com>
3. **[06-26 20:04]** [PATCH v3 02/22] arm64: Generate sign macro for sysreg Enums
   - 发件人: Colton Lewis <coltonlewis@google.com>
4. **[06-26 20:04]** [PATCH v3 03/22] KVM: arm64: Define PMI{CNTR,FILTR}_EL0 as undef_access
   - 发件人: Colton Lewis <coltonlewis@google.com>
5. **[06-26 20:04]** [PATCH v3 04/22] KVM: arm64: Cleanup PMU includes
   - 发件人: Colton Lewis <coltonlewis@google.com>
6. **[06-26 20:04]** [PATCH v3 05/22] KVM: arm64: Reorganize PMU functions
   - 发件人: Colton Lewis <coltonlewis@google.com>
7. **[06-26 20:04]** [PATCH v3 06/22] perf: arm_pmuv3: Introduce method to partition the PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
8. **[06-26 20:04]** [PATCH v3 07/22] perf: arm_pmuv3: Generalize counter bitmasks
   - 发件人: Colton Lewis <coltonlewis@google.com>
9. **[06-26 20:04]** [PATCH v3 08/22] perf: arm_pmuv3: Keep out of guest counter partition
   - 发件人: Colton Lewis <coltonlewis@google.com>
10. **[06-26 20:04]** [PATCH v3 09/22] KVM: arm64: Correct kvm_arm_pmu_get_max_counters()
   - 发件人: Colton Lewis <coltonlewis@google.com>
11. **[06-26 20:04]** [PATCH v3 10/22] KVM: arm64: Set up FGT for Partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
12. **[06-26 20:04]** [PATCH v3 11/22] KVM: arm64: Writethrough trapped PMEVTYPER register
   - 发件人: Colton Lewis <coltonlewis@google.com>
13. **[06-26 20:04]** [PATCH v3 12/22] KVM: arm64: Use physical PMSELR for PMXEVTYPER if partitioned
   - 发件人: Colton Lewis <coltonlewis@google.com>
14. **[06-26 20:04]** [PATCH v3 13/22] KVM: arm64: Writethrough trapped PMOVS register
   - 发件人: Colton Lewis <coltonlewis@google.com>
15. **[06-26 20:04]** [PATCH v3 14/22] KVM: arm64: Write fast path PMU register handlers
   - 发件人: Colton Lewis <coltonlewis@google.com>
16. **[06-26 20:04]** [PATCH v3 15/22] KVM: arm64: Setup MDCR_EL2 to handle a partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
17. **[06-26 20:04]** [PATCH v3 16/22] KVM: arm64: Account for partitioning in PMCR_EL0 access
   - 发件人: Colton Lewis <coltonlewis@google.com>
18. **[06-26 20:04]** [PATCH v3 17/22] KVM: arm64: Context swap Partitioned PMU guest registers
   - 发件人: Colton Lewis <coltonlewis@google.com>
19. **[06-26 20:04]** [PATCH v3 18/22] KVM: arm64: Enforce PMU event filter at vcpu_load()
   - 发件人: Colton Lewis <coltonlewis@google.com>
20. **[06-26 20:04]** [PATCH v3 19/22] perf: arm_pmuv3: Handle IRQs for Partitioned PMU
 guest counters
   - 发件人: Colton Lewis <coltonlewis@google.com>
21. **[06-26 20:04]** [PATCH v3 20/22] KVM: arm64: Inject recorded guest interrupts
   - 发件人: Colton Lewis <coltonlewis@google.com>
22. **[06-26 20:04]** [PATCH v3 21/22] KVM: arm64: Add ioctl to partition the PMU when supported
   - 发件人: Colton Lewis <coltonlewis@google.com>
23. **[06-26 20:04]** [PATCH v3 22/22] KVM: arm64: selftests: Add test case for partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
24. **[06-27 10:04]** Re: [PATCH v3 02/22] arm64: Generate sign macro for sysreg Enums
   - 发件人: Ben Horgan <ben.horgan@arm.com>
25. **[06-27 14:23]** Re: [PATCH v3 02/22] arm64: Generate sign macro for sysreg Enums
   - 发件人: Marc Zyngier <maz@kernel.org>
26. **[06-27 14:31]** Re: [PATCH v3 03/22] KVM: arm64: Define PMI{CNTR,FILTR}_EL0 as undef_access
   - 发件人: Marc Zyngier <maz@kernel.org>
27. **[06-27 14:36]** Re: [PATCH v3 09/22] KVM: arm64: Correct kvm_arm_pmu_get_max_counters()
   - 发件人: Marc Zyngier <maz@kernel.org>
28. **[06-27 16:01]** Re: [PATCH v3 10/22] KVM: arm64: Set up FGT for Partitioned PMU
   - 发件人: Marc Zyngier <maz@kernel.org>
29. **[06-27 20:45]** Re: [PATCH v3 02/22] arm64: Generate sign macro for sysreg Enums
   - 发件人: Colton Lewis <coltonlewis@google.com>
30. **[06-27 20:45]** Re: [PATCH v3 03/22] KVM: arm64: Define PMI{CNTR,FILTR}_EL0 as undef_access
   - 发件人: Colton Lewis <coltonlewis@google.com>
31. **[06-27 20:45]** Re: [PATCH v3 10/22] KVM: arm64: Set up FGT for Partitioned PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
32. **[06-27 13:55]** Re: [PATCH v3 02/22] arm64: Generate sign macro for sysreg Enums
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
33. **[06-28 09:25]** Re: [PATCH v3 10/22] KVM: arm64: Set up FGT for Partitioned PMU
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [PATCH v6 00/28] KVM: arm64: Implement support for SME

**📧 邮件数**: 31 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 25 Jun 2025 11:47:51 +0100

#### 🤖 AI 总结

本邮件线程讨论了 KVM（Kernel-based Virtual Machine）在 arm64 架构上对 SME（Scalable Matrix Extension）支持的实现，主要围绕一系列补丁（patch）进行。以下是讨论的要点：

1. **原始补丁内容**：补丁系列的核心是实现对 SME 的支持，特别是在非保护的 KVM 客户端中。SME 引入了新的向量长度和控制寄存器，类似于 SVE（Scalable Vector Extension），并允许在流模式下使用 SVE 寄存器。

2. **历史讨论要点**：之前的讨论集中在如何处理 SME 和 SVE 的寄存器访问、状态保存与恢复，以及如何在 KVM 中实现这些功能。补丁中提到，SME 的实现必须与 SVE 的实现相协调，以避免复杂的状态管理。

3. **本周的新讨论与进展**：本周的讨论主要集中在补丁的具体实现细节上，包括：
   - 引入新的系统寄存器（如 SMCR、SMIDR）以支持 SME。
   - 处理 SME 的异常和控制寄存器的访问。
   - 允许嵌套虚拟机访问 SME 状态。
   - 讨论了如何在用户空间访问 SME 特定寄存器（如 ZA 和 ZT0）。
   - 解决了对 SME 优先级寄存器的支持问题，并确保这些寄存器在 KVM 中的行为符合预期。

此外，Marc Zyngier 对某些寄存器的实现提出了质疑，认为某些寄存器的设计不必要增加复杂性，并建议应保持一致性以避免潜在的错误。这些讨论表明，KVM 对 SME 的支持仍在不断完善中，涉及到的技术细节和实现方式需要进一步的审查和优化。

#### 📝 邮件列表

1. **[06-25 11:47]** [PATCH v6 00/28] KVM: arm64: Implement support for SME
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[06-25 11:47]** [PATCH v6 01/28] arm64/fpsimd: Update FA64 and ZT0 enables when
 loading SME state
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[06-25 11:47]** [PATCH v6 02/28] arm64/fpsimd: Decide to save ZT0 and streaming
 mode FFR at bind time
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[06-25 11:47]** [PATCH v6 03/28] arm64/fpsimd: Check enable bit for FA64 when
 saving EFI state
   - 发件人: Mark Brown <broonie@kernel.org>
5. **[06-25 11:47]** [PATCH v6 04/28] arm64/fpsimd: Determine maximum virtualisable SME
 vector length
   - 发件人: Mark Brown <broonie@kernel.org>
6. **[06-25 11:47]** [PATCH v6 05/28] KVM: arm64: Introduce non-UNDEF FGT control
   - 发件人: Mark Brown <broonie@kernel.org>
7. **[06-25 11:47]** [PATCH v6 06/28] KVM: arm64: Pay attention to FFR parameter in SVE
 save and load
   - 发件人: Mark Brown <broonie@kernel.org>
8. **[06-25 11:47]** [PATCH v6 07/28] KVM: arm64: Pull ctxt_has_ helpers to start of
 sysreg-sr.h
   - 发件人: Mark Brown <broonie@kernel.org>
9. **[06-25 11:47]** [PATCH v6 08/28] KVM: arm64: Move SVE state access macros after
 feature test macros
   - 发件人: Mark Brown <broonie@kernel.org>
10. **[06-25 11:48]** [PATCH v6 09/28] KVM: arm64: Rename SVE finalization constants to
 be more general
   - 发件人: Mark Brown <broonie@kernel.org>
11. **[06-25 11:48]** [PATCH v6 10/28] KVM: arm64: Document the KVM ABI for SME
   - 发件人: Mark Brown <broonie@kernel.org>
12. **[06-25 11:48]** [PATCH v6 11/28] KVM: arm64: Define internal features for SME
   - 发件人: Mark Brown <broonie@kernel.org>
13. **[06-25 11:48]** [PATCH v6 12/28] KVM: arm64: Rename sve_state_reg_region
   - 发件人: Mark Brown <broonie@kernel.org>
14. **[06-25 11:48]** [PATCH v6 13/28] KVM: arm64: Store vector lengths in an array
   - 发件人: Mark Brown <broonie@kernel.org>
15. **[06-25 11:48]** [PATCH v6 14/28] KVM: arm64: Implement SME vector length
 configuration
   - 发件人: Mark Brown <broonie@kernel.org>
16. **[06-25 11:48]** [PATCH v6 15/28] KVM: arm64: Support SME control registers
   - 发件人: Mark Brown <broonie@kernel.org>
17. **[06-25 11:48]** [PATCH v6 16/28] KVM: arm64: Support TPIDR2_EL0
   - 发件人: Mark Brown <broonie@kernel.org>
18. **[06-25 11:48]** [PATCH v6 17/28] KVM: arm64: Support SME identification registers
 for guests
   - 发件人: Mark Brown <broonie@kernel.org>
19. **[06-25 11:48]** [PATCH v6 18/28] KVM: arm64: Support SME priority registers
   - 发件人: Mark Brown <broonie@kernel.org>
20. **[06-25 11:48]** [PATCH v6 19/28] KVM: arm64: Provide assembly for SME register
 access
   - 发件人: Mark Brown <broonie@kernel.org>
21. **[06-25 11:48]** [PATCH v6 20/28] KVM: arm64: Support userspace access to streaming
 mode Z and P registers
   - 发件人: Mark Brown <broonie@kernel.org>
22. **[06-25 11:48]** [PATCH v6 21/28] KVM: arm64: Flush register state on writes to
 SVCR.SM and SVCR.ZA
   - 发件人: Mark Brown <broonie@kernel.org>
23. **[06-25 11:48]** [PATCH v6 22/28] KVM: arm64: Expose SME specific state to
 userspace
   - 发件人: Mark Brown <broonie@kernel.org>
24. **[06-25 11:48]** [PATCH v6 23/28] KVM: arm64: Context switch SME state for guests
   - 发件人: Mark Brown <broonie@kernel.org>
25. **[06-25 11:48]** [PATCH v6 24/28] KVM: arm64: Handle SME exceptions
   - 发件人: Mark Brown <broonie@kernel.org>
26. **[06-25 11:48]** [PATCH v6 25/28] KVM: arm64: Expose SME to nested guests
   - 发件人: Mark Brown <broonie@kernel.org>
27. **[06-25 11:48]** [PATCH v6 26/28] KVM: arm64: Provide interface for configuring and
 enabling SME for guests
   - 发件人: Mark Brown <broonie@kernel.org>
28. **[06-25 11:48]** [PATCH v6 27/28] KVM: arm64: selftests: Add SME system registers
 to get-reg-list
   - 发件人: Mark Brown <broonie@kernel.org>
29. **[06-25 11:48]** [PATCH v6 28/28] KVM: arm64: selftests: Add SME to set_id_regs
 test
   - 发件人: Mark Brown <broonie@kernel.org>
30. **[06-29 10:32]** Re: [PATCH v6 18/28] KVM: arm64: Support SME priority registers
   - 发件人: Marc Zyngier <maz@kernel.org>
31. **[06-29 11:08]** Re: [PATCH v6 17/28] KVM: arm64: Support SME identification registers for guests
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 3: [PATCH v9 00/43] arm64: Support for Arm CCA in KVM

**📧 邮件数**: 26 | **👥 参与者**: 7 | **📅 开始时间**: Wed, 11 Jun 2025 11:47:57 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 Arm Confidential Compute Architecture (CCA) 的 KVM 支持的第九版补丁（PATCH v9 00/43）。该补丁系列旨在为 KVM 提供运行受保护虚拟机的能力，相关的来宾支持已在 v6.14-rc1 中合并。

在历史讨论中，补丁的主要内容包括创建和配置领域的 ioctl、内存运行时故障处理、以及允许虚拟机监控器（VMM）设置内存页面的状态等。参与者对补丁的多个部分进行了审查和讨论，提出了一些小的修改建议和代码优化。

在本周的新讨论中，参与者针对补丁中的具体实现细节进行了深入探讨。例如，针对某些变量未初始化的问题，Steven Price 和 Yiwei Zhuang 进行了有效的沟通，确认了需要添加初始化代码。此外，Emi Kisanuki 提到他们在内部模拟器上测试了该补丁，结果符合预期，所有测试通过，除了 PMU（性能监控单元）因不支持而未通过。

总体来看，本周的讨论集中在补丁的细节修正和测试结果上，推动了补丁的进一步完善和验证。

#### 📝 邮件列表

1. **[06-11 11:47]** [PATCH v9 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>
2. **[06-11 11:48]** [PATCH v9 07/43] arm64: RME: ioctls to create and configure realms
   - 发件人: Steven Price <steven.price@arm.com>
3. **[06-11 11:48]** [PATCH v9 10/43] arm64: RME: RTT tear down
   - 发件人: Steven Price <steven.price@arm.com>
4. **[06-11 11:48]** [PATCH v9 11/43] arm64: RME: Allocate/free RECs to match vCPUs
   - 发件人: Steven Price <steven.price@arm.com>
5. **[06-11 11:48]** [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Steven Price <steven.price@arm.com>
6. **[06-11 11:48]** [PATCH v9 16/43] arm64: RME: Handle realm enter/exit
   - 发件人: Steven Price <steven.price@arm.com>
7. **[06-11 11:48]** [PATCH v9 20/43] arm64: RME: Runtime faulting of memory
   - 发件人: Steven Price <steven.price@arm.com>
8. **[06-11 11:48]** [PATCH v9 22/43] KVM: arm64: Validate register access for a Realm VM
   - 发件人: Steven Price <steven.price@arm.com>
9. **[06-11 11:48]** [PATCH v9 28/43] arm64: RME: Allow checking SVE on VM instance
   - 发件人: Steven Price <steven.price@arm.com>
10. **[06-16 11:41]** Re: [PATCH v9 10/43] arm64: RME: RTT tear down
   - 发件人: Suzuki K Poulose <suzuki.poulose@arm.com>
11. **[06-16 21:55]** Re: [PATCH v9 20/43] arm64: RME: Runtime faulting of memory
   - 发件人: Gavin Shan <gshan@redhat.com>
12. **[06-17 20:56]** Re: [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: zhuangyiwei <zhuangyiwei@huawei.com>
13. **[06-18 13:33]** Re: [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Andre Przywara <andre.przywara@arm.com>
14. **[06-23 21:17]** Re: [PATCH v9 07/43] arm64: RME: ioctls to create and configure
 realms
   - 发件人: zhuangyiwei <zhuangyiwei@huawei.com>
15. **[06-23 15:45]** Re: [PATCH v9 07/43] arm64: RME: ioctls to create and configure
 realms
   - 发件人: Steven Price <steven.price@arm.com>
16. **[06-23 15:45]** Re: [PATCH v9 10/43] arm64: RME: RTT tear down
   - 发件人: Steven Price <steven.price@arm.com>
17. **[06-23 15:45]** Re: [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Steven Price <steven.price@arm.com>
18. **[06-23 15:45]** Re: [PATCH v9 15/43] arm64: RME: Allow VMM to set RIPAS
   - 发件人: Steven Price <steven.price@arm.com>
19. **[06-23 17:04]** Re: [PATCH v9 20/43] arm64: RME: Runtime faulting of memory
   - 发件人: Steven Price <steven.price@arm.com>
20. **[06-24 13:50]** Re: [PATCH v9 28/43] arm64: RME: Allow checking SVE on VM instance
   - 发件人: Joey Gouly <joey.gouly@arm.com>
21. **[06-24 16:10]** Re: [PATCH v9 22/43] KVM: arm64: Validate register access for a
 Realm VM
   - 发件人: Joey Gouly <joey.gouly@arm.com>
22. **[06-25 01:45]** RE: [PATCH v9 16/43] arm64: RME: Handle realm enter/exit
   - 发件人: Emi Kisanuki (Fujitsu) <fj0570is@fujitsu.com>
23. **[06-25 01:51]** RE: [PATCH v9 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Emi Kisanuki (Fujitsu) <fj0570is@fujitsu.com>
24. **[06-25 10:00]** Re: [PATCH v9 11/43] arm64: RME: Allocate/free RECs to match vCPUs
   - 发件人: Joey Gouly <joey.gouly@arm.com>
25. **[06-27 11:37]** Re: [PATCH v9 11/43] arm64: RME: Allocate/free RECs to match vCPUs
   - 发件人: Steven Price <steven.price@arm.com>
26. **[06-27 11:37]** Re: [PATCH v9 00/43] arm64: Support for Arm CCA in KVM
   - 发件人: Steven Price <steven.price@arm.com>

---

### Thread 4: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the host
 for software protected VMs

**📧 邮件数**: 20 | **👥 参与者**: 5 | **📅 开始时间**: Wed, 11 Jun 2025 14:33:12 +0100

#### 🤖 AI 总结

本邮件线程讨论了一个关于 KVM（内核虚拟机）映射 guest_memfd 支持的内存的补丁系列，旨在为软件保护的虚拟机提供支持。该补丁系列的主要内容是允许在主机上映射由 guest_memfd 支持的内存，这对像 Firecracker 这样的虚拟机管理程序尤为重要。

在历史讨论中，补丁的主要变更包括对之前反馈的响应、基于 Linux 6.16-rc1 的重基，以及对内存映射和共享内存的支持。参与者们讨论了补丁中一些函数和标志的命名，以提高代码的可读性和准确性。

本周的新讨论中，Fuad Tabba 提出了 V13 版本的计划变更，包括在结构体中添加 `supports_gmem` 布尔值而不是重命名现有的 `has_private_mem`。此外，参与者们一致同意将一些标志和函数的名称进行调整，以便更好地反映其功能。讨论还涉及到如何在同一虚拟机中同时支持和不支持 mmap 的 guest_memfd memslot，以满足用户的不同需求。最终，参与者们达成共识，认为引入一个新的 VM 级别标志 KVM_CAP_PREFER_GMEM 将有助于解决当前的设计问题。

总体而言，本周的讨论集中在补丁的命名、功能调整以及如何更好地支持不同类型的内存映射需求上，推动了补丁的进一步完善。

#### 📝 邮件列表

1. **[06-11 14:33]** [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the host
 for software protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
2. **[06-11 14:33]** [PATCH v12 04/18] KVM: x86: Rename kvm->arch.has_private_mem to kvm->arch.supports_gmem
   - 发件人: Fuad Tabba <tabba@google.com>
3. **[06-11 14:33]** [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Fuad Tabba <tabba@google.com>
4. **[06-11 14:33]** [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Fuad Tabba <tabba@google.com>
5. **[06-12 19:38]** Re: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the
 host for software protected VMs
   - 发件人: David Hildenbrand <david@redhat.com>
6. **[06-13 13:35]** Re: [PATCH v12 04/18] KVM: x86: Rename kvm->arch.has_private_mem to kvm->arch.supports_gmem
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[06-13 15:08]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Sean Christopherson <seanjc@google.com>
8. **[06-24 11:02]** Re: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the
 host for software protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
9. **[06-24 12:16]** Re: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the
 host for software protected VMs
   - 发件人: David Hildenbrand <david@redhat.com>
10. **[06-24 11:25]** Re: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the
 host for software protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
11. **[06-24 13:44]** Re: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the
 host for software protected VMs
   - 发件人: David Hildenbrand <david@redhat.com>
12. **[06-24 12:58]** Re: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the
 host for software protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
13. **[06-24 10:50]** Re: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the
 host for software protected VMs
   - 发件人: Sean Christopherson <seanjc@google.com>
14. **[06-24 13:51]** Re: [PATCH v12 04/18] KVM: x86: Rename kvm->arch.has_private_mem to kvm->arch.supports_gmem
   - 发件人: Ackerley Tng <ackerleytng@google.com>
15. **[06-24 16:40]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Ackerley Tng <ackerleytng@google.com>
16. **[06-25 06:33]** Re: [PATCH v12 04/18] KVM: x86: Rename kvm->arch.has_private_mem to
 kvm->arch.supports_gmem
   - 发件人: Roy, Patrick <roypat@amazon.co.uk>
17. **[06-25 09:00]** Re: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the
 host for software protected VMs
   - 发件人: Fuad Tabba <tabba@google.com>
18. **[06-25 07:07]** Re: [PATCH v12 00/18] KVM: Mapping guest_memfd backed memory at the
 host for software protected VMs
   - 发件人: Sean Christopherson <seanjc@google.com>
19. **[06-25 14:47]** Re: [PATCH v12 08/18] KVM: guest_memfd: Allow host to map guest_memfd pages
   - 发件人: Ackerley Tng <ackerleytng@google.com>
20. **[06-27 08:01]** Re: [PATCH v12 10/18] KVM: x86/mmu: Handle guest page faults for
 guest_memfd with shared memory
   - 发件人: Ackerley Tng <ackerleytng@google.com>

---

### Thread 5: [PATCH 1/5] irqchip/gic-v5: Skip deactivate for forwarded PPI
 interrupts

**📧 邮件数**: 17 | **👥 参与者**: 4 | **📅 开始时间**: Fri, 20 Jun 2025 16:07:50 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于在 GICv5 主机上支持 GICv3 客户机的补丁系列，特别是第一个补丁「[PATCH 1/5] irqchip/gic-v5: Skip deactivate for forwarded PPI interrupts」。该补丁的主要内容是当 PPI 中断被转发到客户机时，跳过停用操作，仅执行结束中断（EOI），依赖客户机在处理注入中断时自行停用虚拟和物理中断。这种做法模仿了原生 GICv3 的行为。

在历史讨论中，参与者探讨了补丁的实现细节，特别是如何确保在 GICv5 主机上正确支持 GICv3 客户机。讨论中提到需要在 KVM GIC 支持和 IRQ 芯片支持两个主要领域进行改动，以确保转发的 PPI 行为一致。

在本周的新讨论中，Sascha Bischoff 和其他参与者对补丁进行了进一步的审查和修改。Lorenzo Pieralisi 对第一个补丁表示认可，并确认了相关修改已完成。此外，针对第二个补丁「[PATCH 2/5] irqchip/gic-v5: Populate struct gic_kvm_info」的讨论也表明，相关工作已按计划推进。整体来看，补丁系列的开发进展顺利，参与者积极反馈并进行必要的调整。

#### 📝 邮件列表

1. **[06-20 16:07]** [PATCH 1/5] irqchip/gic-v5: Skip deactivate for forwarded PPI
 interrupts
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[06-20 16:07]** [PATCH 0/5] KVM: arm64: Enable GICv3 guests on GICv5 hosts using
 FEAT_GCIE_LEGACY
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
3. **[06-20 16:07]** [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
4. **[06-20 16:07]** [PATCH 2/5] irqchip/gic-v5: Populate struct gic_kvm_info
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
5. **[06-20 16:07]** [PATCH 5/5] KVM: arm64: gic-v5: Probe for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
6. **[06-20 13:20]** Re: [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[06-20 13:25]** Re: [PATCH 5/5] KVM: arm64: gic-v5: Probe for GICv5
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
8. **[06-20 16:02]** Re: [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[06-22 13:19]** Re: [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Marc Zyngier <maz@kernel.org>
10. **[06-22 05:37]** Re: [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
11. **[06-23 13:02]** Re: [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
12. **[06-23 13:11]** Re: [PATCH 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
13. **[06-23 13:12]** Re: [PATCH 5/5] KVM: arm64: gic-v5: Probe for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
14. **[06-23 17:14]** Re: [PATCH 2/5] irqchip/gic-v5: Populate struct gic_kvm_info
   - 发件人: Lorenzo Pieralisi <lpieralisi@kernel.org>
15. **[06-23 17:21]** Re: [PATCH 1/5] irqchip/gic-v5: Skip deactivate for forwarded PPI
 interrupts
   - 发件人: Lorenzo Pieralisi <lpieralisi@kernel.org>
16. **[06-27 09:49]** Re: [PATCH 1/5] irqchip/gic-v5: Skip deactivate for forwarded PPI
 interrupts
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
17. **[06-27 09:49]** Re: [PATCH 2/5] irqchip/gic-v5: Populate struct gic_kvm_info
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>

---

### Thread 6: [PATCH v3 00/62] KVM: iommu: Overhaul device posted IRQs support

**📧 邮件数**: 13 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 11 Jun 2025 15:45:03 -0700

#### 🤖 AI 总结

本邮件列表讨论的主题是关于 KVM（内核虚拟机）中 IOMMU（输入输出内存管理单元）设备中断支持的全面改进，具体体现在一系列补丁（PATCH v3 00/62）中。

**原始补丁内容**：
补丁系列的第一个补丁是针对 arm64 的修复，主要涉及设备中断的处理和虚拟化支持。补丁中还包括多个针对 SVM（安全虚拟机）的改进，例如增加 `enable_ipiv` 参数以控制 IPI（中断处理器间中断）虚拟化的启用与禁用。

**之前讨论要点**：
在历史讨论中，参与者探讨了如何处理 IPI 虚拟化的问题，特别是在 AMD CPU 存在 erratum #1235 的情况下，强调了在特定 CPU 上禁用 IPI 虚拟化的重要性。此外，讨论中还提到了一些补丁的具体实现细节和潜在的性能影响。

**本周的新讨论与进展**：
本周的讨论中，Naveen N Rao 对多个补丁进行了审查并给予了认可，特别是关于 `enable_ipiv` 和 IPI 虚拟化的补丁。Sean Christopherson 对补丁的应用和细节进行了更新，确认已将大部分补丁应用到 kvm-x86 中，并对一些补丁进行了小幅修改以回应反馈。此外，讨论中还涉及了对 IRQ 阻塞处理的注释改进，以提高代码的可读性和理解性。

总体来看，讨论围绕着如何优化 KVM 中的中断处理机制，确保在不同硬件平台上的稳定性和性能。

#### 📝 邮件列表

1. **[06-11 15:45]** [PATCH v3 00/62] KVM: iommu: Overhaul device posted IRQs support
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[06-11 15:45]** [PATCH v3 17/62] KVM: SVM: Add enable_ipiv param, never set IsRunning
 if disabled
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[06-11 15:45]** [PATCH v3 18/62] KVM: SVM: Disable (x2)AVIC IPI virtualization if CPU
 has erratum #1235
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[06-11 15:45]** [PATCH v3 20/62] KVM: SVM: Add a comment to explain why
 avic_vcpu_blocking() ignores IRQ blocking
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[06-19 17:01]** Re: [PATCH v3 17/62] KVM: SVM: Add enable_ipiv param, never set
 IsRunning if disabled
   - 发件人: Naveen N Rao <naveen@kernel.org>
6. **[06-20 07:39]** Re: [PATCH v3 17/62] KVM: SVM: Add enable_ipiv param, never set
 IsRunning if disabled
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[06-23 16:15]** Re: [PATCH v3 17/62] KVM: SVM: Add enable_ipiv param, never set
 IsRunning if disabled
   - 发件人: Naveen N Rao <naveen@kernel.org>
8. **[06-23 19:35]** Re: [PATCH v3 18/62] KVM: SVM: Disable (x2)AVIC IPI virtualization
 if CPU has erratum #1235
   - 发件人: Naveen N Rao <naveen@kernel.org>
9. **[06-23 08:30]** Re: [PATCH v3 18/62] KVM: SVM: Disable (x2)AVIC IPI virtualization if
 CPU has erratum #1235
   - 发件人: Sean Christopherson <seanjc@google.com>
10. **[06-23 21:24]** Re: [PATCH v3 20/62] KVM: SVM: Add a comment to explain why
 avic_vcpu_blocking() ignores IRQ blocking
   - 发件人: Naveen N Rao <naveen@kernel.org>
11. **[06-23 09:18]** Re: [PATCH v3 20/62] KVM: SVM: Add a comment to explain why
 avic_vcpu_blocking() ignores IRQ blocking
   - 发件人: Sean Christopherson <seanjc@google.com>
12. **[06-24 12:38]** Re: [PATCH v3 00/62] KVM: iommu: Overhaul device posted IRQs support
   - 发件人: Sean Christopherson <seanjc@google.com>
13. **[06-25 20:58]** Re: [PATCH v3 20/62] KVM: SVM: Add a comment to explain why
 avic_vcpu_blocking() ignores IRQ blocking
   - 发件人: Naveen N Rao <naveen@kernel.org>

---

### Thread 7: [PATCH v3 0/7] Add support for FEAT_{LS64, LS64_V} and related tests

**📧 邮件数**: 12 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 26 Jun 2025 16:08:59 +0800

#### 🤖 AI 总结

本邮件线程讨论了对 Armv8.7 中引入的 FEAT_{LS64, LS64_V} 特性的支持，主要涉及对 64 字节原子加载和存储指令的实现及其在虚拟化环境中的处理。

1. **原始 patch/问题内容**：
   Yicong Yang 提出了一个包含 7 个补丁的系列，旨在为 FEAT_{LS64, LS64_V} 提供支持。这些补丁包括在 CPU 特性列表中添加识别和启用这些特性、通过 HWCAP3 和 cpuinfo 向用户空间暴露支持、添加相关的硬件能力测试，并处理虚拟机中对不支持内存访问的陷阱。

2. **之前讨论要点**：
   之前的讨论主要集中在如何在虚拟化环境中处理 LS64 指令的异常情况，尤其是当访问不支持的内存类型时，是否应该将异常直接注入到用户空间。Marc Zyngier 提出了一些对当前实现的质疑，认为在某些情况下不应涉及虚拟机监控器（VMM）。

3. **本周的新讨论、进展或结论**：
   本周的讨论中，Yicong Yang 更新了补丁，处理了 LS64 指令在不支持的内存上的数据中止（DABT），并允许用户空间注入不支持的排他/原子 DABT。讨论中还提到，是否应将 LS64 支持限制在支持 LS64WB 的硬件上，以便更好地处理异常。最终，参与者达成共识，认为应将不支持的异常直接注入到虚拟机中，而不通过 VMM 处理。整体上，补丁系列得到了进一步的完善和测试，确保其在虚拟化环境中的有效性。

#### 📝 邮件列表

1. **[06-26 16:08]** [PATCH v3 0/7] Add support for FEAT_{LS64, LS64_V} and related tests
   - 发件人: Yicong Yang <yangyicong@huawei.com>
2. **[06-26 16:09]** [PATCH v3 1/7] KVM: arm64: Add exit to userspace on {LD,ST}64B* outside of memslots
   - 发件人: Yicong Yang <yangyicong@huawei.com>
3. **[06-26 16:09]** [PATCH v3 2/7] KVM: arm64: Add documentation for KVM_EXIT_ARM_LDST64B
   - 发件人: Yicong Yang <yangyicong@huawei.com>
4. **[06-26 16:09]** [PATCH v3 3/7] KVM: arm64: Handle DABT caused by LS64* instructions on unsupported memory
   - 发件人: Yicong Yang <yangyicong@huawei.com>
5. **[06-26 16:09]** [PATCH v3 4/7] KVM: arm/arm64: Allow user injection of unsupported exclusive/atomic DABT
   - 发件人: Yicong Yang <yangyicong@huawei.com>
6. **[06-26 16:09]** [PATCH v3 5/7] arm64: Provide basic EL2 setup for FEAT_{LS64, LS64_V} usage at EL0/1
   - 发件人: Yicong Yang <yangyicong@huawei.com>
7. **[06-26 16:09]** [PATCH v3 6/7] arm64: Add support for FEAT_{LS64, LS64_V}
   - 发件人: Yicong Yang <yangyicong@huawei.com>
8. **[06-26 16:09]** [PATCH v3 7/7] KVM: arm64: Enable FEAT_{LS64, LS64_V} in the supported guest
   - 发件人: Yicong Yang <yangyicong@huawei.com>
9. **[06-26 16:11]** Re: [PATCH v3 4/7] KVM: arm/arm64: Allow user injection of
 unsupported exclusive/atomic DABT
   - 发件人: Yicong Yang <yangyicong@huawei.com>
10. **[06-26 09:51]** Re: [PATCH v3 3/7] KVM: arm64: Handle DABT caused by LS64* instructions on unsupported memory
   - 发件人: Marc Zyngier <maz@kernel.org>
11. **[06-26 19:39]** Re: [PATCH v3 3/7] KVM: arm64: Handle DABT caused by LS64*
 instructions on unsupported memory
   - 发件人: Yicong Yang <yangyicong@huawei.com>
12. **[06-27 14:12]** Re: [PATCH v3 3/7] KVM: arm64: Handle DABT caused by LS64* instructions on unsupported memory
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 8: [PATCH v2 01/23] arm64: cpufeature: Add cpucap for HPMN0

**📧 邮件数**: 11 | **👥 参与者**: 2 | **📅 开始时间**: Fri, 20 Jun 2025 17:44:14 -0700

#### 🤖 AI 总结

本邮件列表讨论的主题是关于一个针对 ARM64 架构的补丁（PATCH v2 01/23），其内容是为 HPMN0 添加 CPU 特性标志（cpucap）。该补丁旨在增强 ARM64 的 CPU 功能描述，以便更好地支持相关硬件特性。

在历史讨论中，Colton Lewis 提出了对补丁的反馈，指出描述字段（.desc）应更具描述性，以保持与其他字段的一致性。Oliver Upton 也对补丁的某些实现细节表示疑虑，特别是与 PMUv3 驱动的兼容性问题。

在本周的新讨论中，Colton Lewis 对之前的反馈进行了回应，表示将根据 Oliver 的建议修改描述字段。此外，关于 PMUv3 驱动的分区方法，Colton 和 Oliver 进行了深入探讨，讨论了如何更好地设计参数以满足不同的需求，特别是如何处理主机和来宾的计数器分配。Colton 最终同意回归使用单一参数来简化实现。

总体来看，本周的讨论集中在补丁的描述性改进和 PMUv3 驱动的设计细节上，参与者们积极交流，推动补丁的完善。

#### 📝 邮件列表

1. **[06-20 17:44]** Re: [PATCH v2 01/23] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[06-20 18:06]** Re: [PATCH v2 07/23] perf: arm_pmuv3: Introduce method to partition
 the PMU
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[06-23 18:25]** Re: [PATCH v2 03/23] arm64: cpufeature: Add cpucap for PMICNTR
   - 发件人: Colton Lewis <coltonlewis@google.com>
4. **[06-23 18:25]** Re: [PATCH v2 01/23] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Colton Lewis <coltonlewis@google.com>
5. **[06-23 18:26]** Re: [PATCH v2 07/23] perf: arm_pmuv3: Introduce method to partition
 the PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
6. **[06-23 22:04]** Re: [PATCH v2 05/23] KVM: arm64: Cleanup PMU includes
   - 发件人: Colton Lewis <coltonlewis@google.com>
7. **[06-23 22:11]** Re: [PATCH v2 17/23] KVM: arm64: Account for partitioning in PMCR_EL0 access
   - 发件人: Colton Lewis <coltonlewis@google.com>
8. **[06-24 00:05]** Re: [PATCH v2 07/23] perf: arm_pmuv3: Introduce method to partition
 the PMU
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
9. **[06-24 00:28]** Re: [PATCH v2 01/23] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
10. **[06-24 20:05]** Re: [PATCH v2 07/23] perf: arm_pmuv3: Introduce method to partition
 the PMU
   - 发件人: Colton Lewis <coltonlewis@google.com>
11. **[06-24 20:05]** Re: [PATCH v2 01/23] arm64: cpufeature: Add cpucap for HPMN0
   - 发件人: Colton Lewis <coltonlewis@google.com>

---

### Thread 9: [PATCH v8 00/14] arm: rework id register storage

**📧 邮件数**: 10 | **👥 参与者**: 4 | **📅 开始时间**: Tue, 17 Jun 2025 17:39:17 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM 架构的 ID 寄存器存储重构的补丁（PATCH v8 00/14）。该补丁主要针对之前 Peter 的反馈进行了修改，确保每个中间阶段都能编译，并增强了脚本的鲁棒性，以便只抓取所需的寄存器。

在历史讨论中，Cornelia Huck 提到补丁的编译测试已完成，并修复了一些问题。此外，Eric Auger 提出了自动生成系统寄存器定义的脚本，旨在简化寄存器定义的生成过程。

在本周的新讨论中，Eric Auger 报告了补丁中出现的多个 checkpatch 错误，包括行长度超过限制和宏定义的复杂性问题。参与者们讨论了是否需要改进 checkpatch.pl 以消除这些错误，并认为某些错误可以被忽略，因为它们出现在不常见的文件中。Peter Maydell 提出，虽然可以修复某些问题，但在可读性方面，保持较长的行可能更好。整体上，参与者们对补丁的进展表示认可，并讨论了如何处理 checkpatch 的反馈。

#### 📝 邮件列表

1. **[06-17 17:39]** [PATCH v8 00/14] arm: rework id register storage
   - 发件人: Cornelia Huck <cohuck@redhat.com>
2. **[06-17 17:39]** [PATCH v8 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Cornelia Huck <cohuck@redhat.com>
3. **[06-17 17:45]** Re: [PATCH v8 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Cornelia Huck <cohuck@redhat.com>
4. **[06-25 11:10]** Re: [PATCH v8 00/14] arm: rework id register storage
   - 发件人: Eric Auger <eric.auger@redhat.com>
5. **[06-25 11:16]** Re: [PATCH v8 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Eric Auger <eric.auger@redhat.com>
6. **[06-25 10:23]** Re: [PATCH v8 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Daniel =?utf-8?B?UC4gQmVycmFuZ8Op?= <berrange@redhat.com>
7. **[06-25 11:24]** Re: [PATCH v8 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Cornelia Huck <cohuck@redhat.com>
8. **[06-25 11:31]** Re: [PATCH v8 12/14] arm/cpu: Add sysreg generation scripts
   - 发件人: Eric Auger <eric.auger@redhat.com>
9. **[06-25 11:14]** Re: [PATCH v8 00/14] arm: rework id register storage
   - 发件人: Peter Maydell <peter.maydell@linaro.org>
10. **[06-25 18:37]** Re: [PATCH v8 00/14] arm: rework id register storage
   - 发件人: Cornelia Huck <cohuck@redhat.com>

---

### Thread 10: [PATCH v5 0/5] KVM: x86: Provide a cap to disable APERF/MPERF read intercepts

**📧 邮件数**: 8 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 25 Jun 2025 17:12:20 -0700

#### 🤖 AI 总结

本邮件主题为“[PATCH v5 0/5] KVM: x86: 提供一个能力以禁用 APERF/MPERF 读取拦截”，共有8封邮件，主要讨论了KVM（内核虚拟机）在x86架构下的相关补丁。

**原始补丁内容**：
该补丁系列旨在允许虚拟机（VM）读取IA32_APERF和IA32_MPERF寄存器，而不触发拦截。这将帮助虚拟机获取物理CPU的有效频率倍增器。

**之前讨论要点**：
补丁的背景是，之前的提交（如b51700632e0e）已经允许用户空间的虚拟机监控器（VMM）授予虚拟机读取四个核心C状态驻留的MSR（模型特定寄存器）的权限。补丁系列的目标是将这一能力扩展到APERF和MPERF寄存器。

**本周新讨论与进展**：
1. 本周的讨论集中在补丁的具体实现上，包括对MSR拦截的重构和自测的扩展。
2. 参与者讨论了如何在VMX和SVM环境下支持对这些寄存器的直接读取，并确保在自测中验证这一功能。
3. Xiaoyao Li对补丁进行了审查，并提出了一些小的修改建议，显示出对补丁的认可。

总体而言，本周的讨论推动了补丁的进展，确保了对新功能的测试和验证，增强了KVM的性能和灵活性。

#### 📝 邮件列表

1. **[06-25 17:12]** [PATCH v5 0/5] KVM: x86: Provide a cap to disable APERF/MPERF read intercepts
   - 发件人: Sean Christopherson <seanjc@google.com>
2. **[06-25 17:12]** [PATCH v5 1/5] KVM: x86: Replace growing set of *_in_guest bools with
 a u64
   - 发件人: Sean Christopherson <seanjc@google.com>
3. **[06-25 17:12]** [PATCH v5 2/5] KVM: x86: Provide a capability to disable APERF/MPERF
 read intercepts
   - 发件人: Sean Christopherson <seanjc@google.com>
4. **[06-25 17:12]** [PATCH v5 3/5] KVM: selftests: Expand set of APIs for pinning tasks
 to a single CPU
   - 发件人: Sean Christopherson <seanjc@google.com>
5. **[06-25 17:12]** [PATCH v5 4/5] KVM: selftests: Test behavior of KVM_X86_DISABLE_EXITS_APERFMPERF
   - 发件人: Sean Christopherson <seanjc@google.com>
6. **[06-25 17:12]** [PATCH v5 5/5] KVM: selftests: Convert arch_timer tests to common
 helpers to pin task
   - 发件人: Sean Christopherson <seanjc@google.com>
7. **[06-26 16:53]** Re: [PATCH v5 1/5] KVM: x86: Replace growing set of *_in_guest bools
 with a u64
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>
8. **[06-26 16:59]** Re: [PATCH v5 2/5] KVM: x86: Provide a capability to disable
 APERF/MPERF read intercepts
   - 发件人: Xiaoyao Li <xiaoyao.li@intel.com>

---

### Thread 11: [PATCH v2 00/27] KVM: arm64: SCTLR2, DoubleFault2, and NV external abort fixes

**📧 邮件数**: 7 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 16 Jun 2025 16:02:41 -0700

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（内核虚拟机）在 arm64 架构上的一系列补丁，主要集中在 SCTLR2、DoubleFault2 和 NV 外部中止的修复。

**原始补丁内容**：Oliver Upton 提交的补丁系列（PATCH v2 00/27）旨在实现 FEAT_RAS、FEAT_SCLTR2 和 FEAT_DoubleFault2 的支持，尤其是针对非虚拟化（NV）和虚拟化（non-NV）环境的处理。这些补丁的关键在于改进错误处理机制，尤其是与 SError 相关的异常路由和掩码处理。

**之前讨论要点**：在历史讨论中，Marc Zyngier 提出了一些关于补丁实现的反馈，特别是关于预取和异常处理的细节。他指出需要考虑虚拟机是否支持 RAS（可靠性、可用性和可维护性），并对异常注入的逻辑提出了质疑。

**本周新讨论**：本周的讨论中，Oliver 对之前的讨论做出了回应，承认了一些实现上的疏漏，并表示已通过修改代码来解决这些问题。他强调了在处理 SError 时需要特别注意的上下文信息，并更新了 KVM_GET_VCPU_EVENTS 以测试相关标志。这些讨论表明，开发者们在确保补丁的正确性和稳定性方面进行了深入的交流和修正。

#### 📝 邮件列表

1. **[06-16 16:02]** [PATCH v2 00/27] KVM: arm64: SCTLR2, DoubleFault2, and NV external abort fixes
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
2. **[06-16 16:02]** [PATCH v2 06/27] KVM: arm64: nv: Honor SError exception routing / masking
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
3. **[06-16 16:02]** [PATCH v2 17/27] KVM: arm64: Route SEAs to the SError vector when EASE is set
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
4. **[06-21 11:47]** Re: [PATCH v2 06/27] KVM: arm64: nv: Honor SError exception routing / masking
   - 发件人: Marc Zyngier <maz@kernel.org>
5. **[06-21 12:54]** Re: [PATCH v2 17/27] KVM: arm64: Route SEAs to the SError vector when EASE is set
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[06-24 01:12]** Re: [PATCH v2 17/27] KVM: arm64: Route SEAs to the SError vector
 when EASE is set
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[06-24 04:44]** Re: [PATCH v2 06/27] KVM: arm64: nv: Honor SError exception routing
 / masking
   - 发件人: Oliver Upton <oliver.upton@linux.dev>

---

### Thread 12: [PATCH v3 0/4] KVM: arm64: Add attribute to control GICD_TYPER2.nASSGIcap

**📧 邮件数**: 7 | **👥 参与者**: 3 | **📅 开始时间**: Fri, 13 Jun 2025 15:52:34 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构中引入一个新属性，以控制 GICD_TYPER2.nASSGIcap 的补丁（PATCH v3 0/4）。该补丁的目的是解决 GIC 架构中对 ITS（Interrupt Translation Service）支持的限制，使得用户能够在每个虚拟机（VM）级别上控制该特性，从而提供更灵活的硬件中断注入支持。

在历史讨论中，Raghavendra Rao Ananta 提出了该补丁，并指出当前 KVM 无条件地宣传 GICD_TYPER2.nASSGIcap，建议允许用户在 VGIC 初始化之前更改 VM 是否支持该特性。Marc Zyngier 提出了对默认行为的关注，并询问是否应该在没有 GICv4.1 的情况下仍然宣传该特性。

在本周的新讨论中，Oliver Upton 和 Marc Zyngier 继续探讨了如何处理 nASSGIcap 的暴露问题。Oliver 认为无条件暴露该能力是有用的，以便用户空间可以依赖它的效果，而 Marc 则担心在用户空间写入 GICD_TYPER2 会带来复杂性。他们讨论了是否应该允许用户空间直接写入 GICD_TYPER2，并认为这可能会导致额外的复杂性，但也没有达成一致的结论。

总体来看，讨论集中在如何平衡用户空间的灵活性与系统复杂性之间，尚未对补丁的最终实现达成一致。

#### 📝 邮件列表

1. **[06-13 15:52]** [PATCH v3 0/4] KVM: arm64: Add attribute to control GICD_TYPER2.nASSGIcap
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
2. **[06-13 15:52]** [PATCH v3 3/4] KVM: arm64: Introduce attribute to control GICD_TYPER2.nASSGIcap
   - 发件人: Raghavendra Rao Ananta <rananta@google.com>
3. **[06-21 09:50]** Re: [PATCH v3 3/4] KVM: arm64: Introduce attribute to control GICD_TYPER2.nASSGIcap
   - 发件人: Marc Zyngier <maz@kernel.org>
4. **[06-23 01:40]** Re: [PATCH v3 3/4] KVM: arm64: Introduce attribute to control
 GICD_TYPER2.nASSGIcap
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
5. **[06-23 10:05]** Re: [PATCH v3 3/4] KVM: arm64: Introduce attribute to control GICD_TYPER2.nASSGIcap
   - 发件人: Marc Zyngier <maz@kernel.org>
6. **[06-23 02:25]** Re: [PATCH v3 3/4] KVM: arm64: Introduce attribute to control
 GICD_TYPER2.nASSGIcap
   - 发件人: Oliver Upton <oliver.upton@linux.dev>
7. **[06-23 15:37]** Re: [PATCH v3 3/4] KVM: arm64: Introduce attribute to control GICD_TYPER2.nASSGIcap
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 13: [PATCH v2 3/5] arm64/sysreg: Add ICH_VCTLR_EL2

**📧 邮件数**: 6 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 27 Jun 2025 10:09:01 +0000

#### 🤖 AI 总结

本邮件线程讨论了一个针对 ARM64 架构的补丁系列，主要目的是在 GICv5 主机上支持 GICv3 客户机。补丁的核心是添加了一个新的系统寄存器 ICH_VCTLR_EL2，以便在 GICv5 主机上启用或禁用 GICv3 兼容模式（FEAT_GCIE_LEGACY）。

在历史讨论中，补丁的主要内容是确保 GICv3 客户机能够在 GICv5 主机上正常运行，而无需对虚拟机或虚拟机监控程序进行修改。补丁系列包括对 KVM GIC 支持的增强、IRQ 芯片支持的改进，以及确保转发的 PPI 中断符合 GICv3 的预期行为。

本周的新讨论中，Sascha Bischoff 提出了多个补丁，具体包括：
1. 添加 ICH_VCTLR_EL2 寄存器的补丁，确保可以控制 GICv3 兼容模式。
2. 更新 gic_kvm_info 结构，以支持 GICv5 主机的探测。
3. 引入 GICv5 的探测功能，确保在检测到 FEAT_GCIE_LEGACY 时能够支持 GICv3 客户机。

这些补丁的实施将使得在 GICv5 系统上运行 GICv3 虚拟机成为可能，提升了系统的兼容性和灵活性。参与者对补丁的反馈积极，表明该系列补丁在社区中得到了认可。

#### 📝 邮件列表

1. **[06-27 10:09]** [PATCH v2 3/5] arm64/sysreg: Add ICH_VCTLR_EL2
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
2. **[06-27 10:09]** [PATCH v2 2/5] irqchip/gic-v5: Populate struct gic_kvm_info
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
3. **[06-27 10:09]** [PATCH v2 0/5] KVM: arm64: Enable GICv3 guests on GICv5 hosts using
 FEAT_GCIE_LEGACY
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
4. **[06-27 10:09]** [PATCH v2 1/5] irqchip/gic-v5: Skip deactivate for forwarded PPI
 interrupts
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
5. **[06-27 10:09]** [PATCH v2 4/5] KVM: arm64: gic-v5: Support GICv3 compat
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>
6. **[06-27 10:09]** [PATCH v2 5/5] KVM: arm64: gic-v5: Probe for GICv5
   - 发件人: Sascha Bischoff <Sascha.Bischoff@arm.com>

---

### Thread 14: [PATCH v6 0/5] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI

**📧 邮件数**: 6 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 27 Jun 2025 07:12:24 +0000

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下支持 FF-A（Firmware Framework for Arm）1.2 版本及其 SEND_DIRECT2 ABI 的一系列补丁。

1. **原始补丁内容**：该补丁集（共5个补丁）旨在实现对 FF-A 1.2 规范的支持，特别是新的 SEND_DIRECT2 ABI。此补丁防止主机使用低于已与虚拟机监控器（hypervisor）协商的 FF-A 版本，确保兼容性。

2. **之前讨论要点**：在之前的讨论中，补丁的主要内容包括对 FF-A 1.2 的支持、与 SMCCC（Secure Monitor Call Convention）1.2 的集成，以及对未实现的 FF-A 1.2 接口的处理。补丁还经过了测试，确保在 QEMU 下运行 Android 时能够成功使用 SEND_DIRECT2 ABI。

3. **本周的新讨论与进展**：本周的讨论中，补丁集的每个部分都进行了详细更新。包括：
   - 第一个补丁修正了主机版本降级尝试时的返回值。
   - 第二个补丁将 FF-A 初始化和主机处理程序更新为使用 SMCCC 1.2。
   - 第三个补丁标记 FFA_NOTIFICATION_* 接口为不支持。
   - 第四个补丁将支持的 FF-A 版本提升至 1.2。
   - 第五个补丁在主机处理程序中添加了对 FFA_MSG_SEND_DIRECT_REQ2 的支持。

整体上，这些补丁的目标是确保 KVM 在 arm64 架构下能够有效支持 FF-A 1.2 及其新特性，提升虚拟化性能和兼容性。

#### 📝 邮件列表

1. **[06-27 07:12]** [PATCH v6 0/5] KVM: arm64: Support FF-A 1.2 and SEND_DIRECT2 ABI
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
2. **[06-27 07:12]** [PATCH v6 1/5] KVM: arm64: Correct return value on host version
 downgrade attempt
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
3. **[06-27 07:12]** [PATCH v6 2/5] KVM: arm64: Use SMCCC 1.2 for FF-A initialization
 and in host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
4. **[06-27 07:12]** [PATCH v6 3/5] KVM: arm64: Mark FFA_NOTIFICATION_* calls as
 unsupported
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
5. **[06-27 07:12]** [PATCH v6 4/5] KVM: arm64: Bump the supported version of FF-A to
 1.2
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>
6. **[06-27 07:12]** [PATCH v6 5/5] KVM: arm64: Support FFA_MSG_SEND_DIRECT_REQ2 in
 host handler
   - 发件人: Per Larsen via B4 Relay <devnull+perlarsen.google.com@kernel.org>

---

### Thread 15: [PATCH 0/3] arm64: Support FEAT_LSFE (Large System Float
 Extension)

**📧 邮件数**: 4 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 27 Jun 2025 18:20:43 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于在 arm64 架构中支持 FEAT_LSFE（大系统浮点扩展）的补丁。FEAT_LSFE 是从 v9.5 版本开始可选的功能，主要用于提供原子浮点内存操作。尽管当前内核并没有对该特性的直接需求，但补丁旨在为用户空间提供硬件能力（hwcap）以便其能够发现这一特性，并允许 KVM 客户端访问相关的 ID 寄存器字段。

在历史讨论中，补丁的主要内容是添加对 FEAT_LSFE 的支持，包括在相关文档和代码中引入 hwcap 标志。补丁的具体实现包括更新头文件、CPU 特性文件以及 KVM 系统寄存器文件。

本周的新讨论中，Mark Brown 提出了三个补丁：
1. **补丁 1**：为 FEAT_LSFE 添加 hwcap 支持，允许用户空间检测该特性。
2. **补丁 2**：在 KVM 中暴露 FEAT_LSFE 相关的 ID 寄存器字段，以便虚拟机能够识别该特性。
3. **补丁 3**：在自测框架中添加对 lsfe 的测试，确保其在运行时的可用性。

这些补丁的推出标志着对 FEAT_LSFE 特性的逐步支持，尽管目前内核并无直接应用需求。

#### 📝 邮件列表

1. **[06-27 18:20]** [PATCH 0/3] arm64: Support FEAT_LSFE (Large System Float
 Extension)
   - 发件人: Mark Brown <broonie@kernel.org>
2. **[06-27 18:20]** [PATCH 1/3] arm64/hwcap: Add hwcap for FEAT_LSFE
   - 发件人: Mark Brown <broonie@kernel.org>
3. **[06-27 18:20]** [PATCH 2/3] KVM: arm64: Expose FEAT_LSFE to guests
   - 发件人: Mark Brown <broonie@kernel.org>
4. **[06-27 18:20]** [PATCH 3/3] kselftest/arm64: Add lsfe to the hwcaps test
   - 发件人: Mark Brown <broonie@kernel.org>

---

### Thread 16: [PATCH v9 0/6] KVM: arm64: Map GPU device memory as cacheable

**📧 邮件数**: 4 | **👥 参与者**: 3 | **📅 开始时间**: Sat, 21 Jun 2025 04:21:05 +0000

#### 🤖 AI 总结

本邮件线程讨论了关于在 KVM（内核虚拟机）中将 GPU 设备内存映射为可缓存的补丁（PATCH v9 0/6）。该补丁旨在解决 Grace 基于平台（如 Grace Hopper/Blackwell Superchips）中 CPU 可访问的缓存一致性 GPU 内存的映射问题。GPU 设备内存本质上是 DDR 内存，具备缓存性、非对齐访问、原子操作及可执行故障处理等特性，因此需要在二级映射中将其设置为 NORMAL。

在历史讨论中，Ankit Agrawal 提出了两个补丁，分别针对 GPU 内存的缓存映射和修复由于 S1 和 S2 映射属性不匹配引发的安全漏洞。当前的 KVM 实现可能导致用户空间的 VMA（虚拟内存区域）为可缓存，但在 S2 中却被映射为不可缓存，从而可能使虚拟机访问到先前虚拟机未清零的过期数据。

在本周的新讨论中，Ankit 提醒大家对补丁进行审查，并且 Will Deacon 提出了对之前讨论的补丁的评论，指出 arm64 的 get_vma_page_shift() 函数错误地假设 VM_PFNMAP VMA 是物理连续的，这可能会影响到映射的安全性。他还提出了关于如何确保 remap_pfn_range() 函数中的保护属性在客体中反映的问题，认为依赖驱动程序始终传递 'vma->vm_page_prot' 是不可靠的。

#### 📝 邮件列表

1. **[06-21 04:21]** [PATCH v9 0/6] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: ankita <ankita@nvidia.com>
2. **[06-21 04:21]** [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: ankita <ankita@nvidia.com>
3. **[06-27 05:03]** Re: [PATCH v9 0/6] KVM: arm64: Map GPU device memory as cacheable
   - 发件人: Ankit Agrawal <ankita@nvidia.com>
4. **[06-27 14:49]** Re: [PATCH v9 3/6] KVM: arm64: Block cacheable PFNMAP mapping
   - 发件人: Will Deacon <will@kernel.org>

---

### Thread 17: [PATCH] KVM: arm64: nv: Fix MI line level calculation in vgic_v3_nested_update_mi()

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 25 Jun 2025 16:47:09 +0800

#### 🤖 AI 总结

本邮件讨论的主题是针对 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在修复 `vgic_v3_nested_update_mi()` 函数中 MI 线级别计算的错误。

**补丁内容**：补丁的核心是修正 MI 线级别的计算逻辑，确保在 `ICH_HCR_EL2.En` 被设置且 `ICH_MISR_EL2` 非零时，正确地断言 vcpu 的 MI 线状态。原有的计算方法使用位与操作（&=），在 vcpu 的 `ICH_MISR_EL2` 的最低有效位未设置时会导致错误。补丁通过调整 `vgic_v3_get_misr()` 的返回值来解决这一问题。

**历史讨论**：本次讨论没有提供之前的历史讨论内容，主要集中在本周的新进展。

**本周新讨论**：本周的讨论中，Wei-Lin Chang 提出了补丁，Marc Zyngier 对其进行了认可，并建议进一步简化代码。经过讨论，双方达成一致，Marc 最终确认将补丁应用到修复分支，并感谢 Wei-Lin 的贡献。补丁已成功应用，提交 ID 为 `af040a9a296044fd4b748786c2516f172a7617f1`。

#### 📝 邮件列表

1. **[06-25 16:47]** [PATCH] KVM: arm64: nv: Fix MI line level calculation in vgic_v3_nested_update_mi()
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
2. **[06-25 17:45]** Re: [PATCH] KVM: arm64: nv: Fix MI line level calculation in vgic_v3_nested_update_mi()
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[06-26 13:57]** Re: [PATCH] KVM: arm64: nv: Fix MI line level calculation in
 vgic_v3_nested_update_mi()
   - 发件人: Wei-Lin Chang <r09922117@csie.ntu.edu.tw>
4. **[06-26 08:52]** Re: [PATCH] KVM: arm64: nv: Fix MI line level calculation in vgic_v3_nested_update_mi()
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 18: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200803

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 26 Jun 2025 20:41:42 +0800

#### 🤖 AI 总结

本邮件讨论的主题是针对 ARM64 架构中的 HIP10 和 HIP10C 处理器的 erratum 162200803 提出的补丁。该补丁旨在解决 GICv4.0 中与虚拟处理单元（vPE）调度相关的硬件缺陷，具体表现为在多个 vPE 同时发送调度命令时，可能会导致某些命令未被调度，从而引发超时问题。为了解决这一问题，补丁建议限制虚拟本地中断（vLPI）的数量至 4096，以确保硬件在处理调度操作时不会超出其能力。

在本周的讨论中，Zhou Wang 提出了补丁的具体实现细节，并指出了在代码中添加了对 vLPI 数量的限制。然而，Marc Zyngier 提出了对补丁的质疑，认为 KVM 并没有强制执行这一限制，可能会导致虚拟机请求超过限制的 vLPI 数量。此外，他还询问在尝试映射超出允许范围的 vLPI 时，是否需要通知虚拟机。Zhou Wang 随后回应，承认在处理 MAPTI 命令时缺少对 vLPI 数量的检查，并讨论了在补丁中是否应添加相关检查的可行性。

总体来看，本周的讨论集中在补丁的有效性和实现细节上，尤其是如何确保对 vLPI 数量的限制得到遵守。

#### 📝 邮件列表

1. **[06-26 20:41]** [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200803
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>
2. **[06-26 14:27]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum 162200803
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[06-27 14:36]** Re: [PATCH] ARM64: errata: Add workaround for HIP10/HIP10C erratum
 162200803
   - 发件人: Zhou Wang <wangzhou1@hisilicon.com>

---

### Thread 19: [PATCH v6] coccinelle: misc: Add field_modify script

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 26 Jun 2025 14:02:20 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于一个名为“field_modify”的Coccinelle脚本的补丁（PATCH v6），旨在通过使用FIELD_MODIFY()宏来替代内核中硬编码的字段修改模式，从而在编译时捕获可能的参数类型错误。

在历史讨论中，补丁经历了多个版本的迭代。最初的版本中，补丁的目标是引入FIELD_MODIFY()宏，并将其应用于内核核心文件中的四个实例。随着版本的更新，补丁逐渐简化了条件选择，移除了不必要的ARM64补丁，并添加了Coccinelle脚本的不同模式（如org、report和context）。

在本周的新讨论中，Luo Jie提交了补丁的第六版，并回应了参与者Markus Elfring的建议，表示将采用格式化字符串字面量来改善函数调用的代码清晰度。Luo Jie承诺将在下一个版本中进行相应的更新，以提高代码的可读性。

总的来说，本周的讨论集中在补丁的细节改进上，参与者对脚本的功能表示认可，并提出了进一步优化的建议。

#### 📝 邮件列表

1. **[06-26 14:02]** [PATCH v6] coccinelle: misc: Add field_modify script
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
2. **[06-26 09:43]** Re: [PATCH v6] coccinelle: misc: Add field_modify script
   - 发件人: Markus Elfring <Markus.Elfring@web.de>
3. **[06-27 12:33]** Re: [PATCH v6] coccinelle: misc: Add field_modify script
   - 发件人: Luo Jie <quic_luoj@quicinc.com>

---

### Thread 20: [PATCH] KVM: arm64: Don't free hyp pages with pKVM on GICv2

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 26 Jun 2025 10:10:14 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，目的是解决在 GICv2（通用中断控制器版本2）上启用 pKVM（保护虚拟机监控器）时出现的主机内核崩溃问题。

**原始补丁内容**：
补丁的核心是修复在启用 pKVM 时，KVM 初始化过程中出现的内存释放错误。具体来说，pKVM 初始化的前半部分在 vgic 探测之前完成，导致在检测到 GICv2 后，仍然保留了 pKVM 的向量设置，而错误路径会错误地释放 hypervisor 分配的内存，包括 EL2 栈和每个 CPU 的页面。补丁通过跟踪已初始化 pKVM 的 CPU，避免在内存清理过程中释放这些仍在使用的页面。

**之前讨论要点**：
在历史讨论中，Marc Zyngier 报告了启用保护模式时的崩溃问题，并指出了 KVM 初始化过程中错误的内存管理逻辑。

**本周新讨论与进展**：
在本周的讨论中，Quentin Perret 提交了补丁，并在 Juno-r1 硬件上进行了测试，结果表明补丁有效，系统没有崩溃。Marc Zyngier 随后确认补丁已应用到修复列表中，并表示感谢。这表明该问题得到了及时解决，补丁已成功集成。

#### 📝 邮件列表

1. **[06-26 10:10]** [PATCH] KVM: arm64: Don't free hyp pages with pKVM on GICv2
   - 发件人: Quentin Perret <qperret@google.com>
2. **[06-26 12:26]** Re: [PATCH] KVM: arm64: Don't free hyp pages with pKVM on GICv2
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[06-26 12:27]** Re: [PATCH] KVM: arm64: Don't free hyp pages with pKVM on GICv2
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 21: [PATCH v2] KVM: arm64: Fix error path in init_hyp_mode()

**📧 邮件数**: 3 | **👥 参与者**: 3 | **📅 开始时间**: Wed, 25 Jun 2025 12:30:58 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在修复 `init_hyp_mode()` 函数中的错误处理路径。

1. **原始补丁内容**：补丁的主要目的是修复在 pKVM 分配 carveout 失败时，错误路径尝试访问未初始化的 nVHE 每个 CPU 基址的 SVE 状态，导致空指针解引用的问题。补丁通过调整内存释放的顺序，确保在释放每个 CPU 指针之前先释放 SVE 状态，从而避免潜在的崩溃。

2. **之前讨论要点**：在之前的讨论中，Quentin 提到释放顺序的问题，并指出需要先释放 SVE 状态。这一问题在 6.12 版本中被发现，并在主干代码中也能重现。

3. **本周的新讨论与进展**：Mostafa Saleh 提交了补丁 v2，并在邮件中提到已根据 Quentin 的反馈进行了修改。Quentin 对补丁进行了审核并给予了认可。Marc Zyngier 随后确认该补丁已被应用于修复中，并感谢 Mostafa 的贡献。

综上所述，本周的讨论集中在补丁的完善和审核上，最终确认了补丁的有效性并进行了合并。

#### 📝 邮件列表

1. **[06-25 12:30]** [PATCH v2] KVM: arm64: Fix error path in init_hyp_mode()
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[06-25 12:35]** Re: [PATCH v2] KVM: arm64: Fix error path in init_hyp_mode()
   - 发件人: Quentin Perret <qperret@google.com>
3. **[06-26 08:53]** Re: [PATCH v2] KVM: arm64: Fix error path in init_hyp_mode()
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 22: [PATCH] KVM: arm64: Fix error path in init_hyp_mode()

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 25 Jun 2025 11:33:01 +0000

#### 🤖 AI 总结

本邮件线程讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的一个补丁，旨在修复 `init_hyp_mode()` 函数中的错误处理路径。

1. **原始补丁内容**：补丁由 Mostafa Saleh 提出，主要解决在 pKVM 分配 carveout 失败时，错误路径尝试解引用未初始化的 nVHE 每个 CPU 基址的 SVE 状态，可能导致访问 NULL 指针的问题。补丁中增加了 NULL 检查，以避免在释放内存时出现错误。

2. **之前讨论要点**：历史讨论部分没有记录，但补丁的提出是基于对 6.12 版本及主分支的观察，表明在特定情况下可能会尝试释放 NULL 指针。

3. **本周的新讨论与进展**：在本周的讨论中，Quentin Perret 对补丁中的额外 NULL 检查表示困惑，并指出 `free_pages()` 在 NULL 上调用应该是安全的。他认为问题在于在释放每个 CPU 页之前解引用 SVE 状态可能导致错误，并建议考虑更改释放顺序。Mostafa 对此表示理解，并计划在后续版本中进行修正。

总体来看，本周的讨论集中在补丁的逻辑合理性及潜在的内存管理问题上，参与者之间的互动有助于进一步完善补丁。

#### 📝 邮件列表

1. **[06-25 11:33]** [PATCH] KVM: arm64: Fix error path in init_hyp_mode()
   - 发件人: Mostafa Saleh <smostafa@google.com>
2. **[06-25 12:22]** Re: [PATCH] KVM: arm64: Fix error path in init_hyp_mode()
   - 发件人: Quentin Perret <qperret@google.com>
3. **[06-25 12:25]** Re: [PATCH] KVM: arm64: Fix error path in init_hyp_mode()
   - 发件人: Mostafa Saleh <smostafa@google.com>

---

### Thread 23: [PATCH v5] coccinelle: misc: Add field_modify script

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Tue, 24 Jun 2025 18:26:59 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于一个新的补丁（PATCH v5），其目的是为 Coccinelle 工具添加一个名为 `field_modify` 的脚本。该脚本旨在查找并建议将手动编码的字段修改模式转换为使用 `FIELD_MODIFY()` API 的形式，从而在编译时捕获可能的参数类型错误。

在历史讨论中，补丁经历了多个版本的修改，主要集中在简化 Coccinelle 脚本的条件选择和移除不必要的 ARM64 补丁。补丁的最终版本还包括了对核心内核文件中四个手动编码 `FIELD_MODIFY()` 实例的转换，确保使用新的 `FIELD_MODIFY()` 宏。

在本周的新讨论中，参与者 Markus Elfring 提出了对脚本中消息格式化的改进建议，建议使用更简洁的字符串格式。对此，Luo Jie 表示赞同并计划在下一个版本中采纳该建议。这表明讨论在不断推进，补丁的质量和可读性有望得到进一步提升。

#### 📝 邮件列表

1. **[06-24 18:26]** [PATCH v5] coccinelle: misc: Add field_modify script
   - 发件人: Luo Jie <quic_luoj@quicinc.com>
2. **[06-24 15:54]** Re: [PATCH v5] coccinelle: misc: Add field_modify script
   - 发件人: Markus Elfring <Markus.Elfring@web.de>
3. **[06-25 14:26]** Re: [PATCH v5] coccinelle: misc: Add field_modify script
   - 发件人: Luo Jie <quic_luoj@quicinc.com>

---

### Thread 24: [PATCH v2 10/14] loongarch: Handle KCOV __init vs inline mismatches

**📧 邮件数**: 3 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 19 Jun 2025 16:55:48 +0800

#### 🤖 AI 总结

本邮件讨论的主题是关于针对 Loongarch 架构处理 KCOV 的 `__init` 与 `inline` 不匹配问题的补丁（PATCH v2 10/14）。该补丁的目的是将相关函数标记为 `__init`，而不是 `__always_inline`，以解决之前在 x86 和 ARM 架构中遇到的类似问题。

在历史讨论中，Huacai Chen 表达了对该补丁的支持，并提到他倾向于将其标记为 `__init`。这为后续的讨论奠定了基础。

在本周的新讨论中，Huacai Chen 表示如果没有异议，他将应用该补丁，并提到已做出相关修改。Kees Cook 对此表示赞同，并感谢 Huacai 的工作，尽管他尚未验证补丁是否真正解决了之前观察到的不匹配问题，但他认为补丁看起来不错，支持 Huacai 的决定。

总结来看，讨论围绕着如何处理 KCOV 的初始化与内联函数的标记问题，经过讨论，参与者达成一致，准备应用补丁。

#### 📝 邮件列表

1. **[06-19 16:55]** Re: [PATCH v2 10/14] loongarch: Handle KCOV __init vs inline mismatches
   - 发件人: Huacai Chen <chenhuacai@kernel.org>
2. **[06-24 20:31]** Re: [PATCH v2 10/14] loongarch: Handle KCOV __init vs inline mismatches
   - 发件人: Huacai Chen <chenhuacai@kernel.org>
3. **[06-24 18:09]** =?US-ASCII?Q?Re=3A_=5BPATCH_v2_10/14=5D_loongarch=3A_Han?=
 =?US-ASCII?Q?dle_KCOV_=5F=5Finit_vs_inline_mismatches?=
   - 发件人: Kees Cook <kees@kernel.org>

---

### Thread 25: [PATCH] KVM: arm64: Adjust range correctly during host stage-2 faults

**📧 邮件数**: 2 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 25 Jun 2025 10:55:48 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下处理主机阶段2故障时的范围调整问题。Quentin Perret 提出了一个补丁（patch），旨在修复 `host_stage2_adjust_range()` 函数中的一个逻辑错误，该函数在处理内存或 MMIO 区域时，试图找到适当大小的块映射。原有的循环条件错误地检查了下一个级别的支持，而非当前级别，可能导致映射的区域超出单个块的覆盖范围。

在之前的讨论中，虽然没有详细记录，但可以推测这个问题并未引起广泛关注，因为它被认为在实际使用中较为罕见，并且并不构成安全隐患。补丁的主要目的是修复该逻辑错误并提高代码的可读性。

在本周的新讨论中，Marc Zyngier 对补丁进行了确认并表示已将其应用于修复列表，标志着该问题的解决。补丁的提交标识为 `e728e705802fec20f65d974a5d5eb91217ac618d`。整体来看，此次讨论有效推动了 KVM 的代码质量提升。

#### 📝 邮件列表

1. **[06-25 10:55]** [PATCH] KVM: arm64: Adjust range correctly during host stage-2 faults
   - 发件人: Quentin Perret <qperret@google.com>
2. **[06-26 08:53]** Re: [PATCH] KVM: arm64: Adjust range correctly during host stage-2 faults
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 26: [PATCH v3 00/13] KVM: Make irqfd registration globally unique

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 24 Jun 2025 12:38:26 -0700

#### 🤖 AI 总结

本邮件主题为“[PATCH v3 00/13] KVM: Make irqfd registration globally unique”，主要讨论了 KVM 中 irqfd 注册的全局唯一性问题。

在历史讨论中，虽然没有具体的邮件记录，但可以推测该补丁的目的是为了确保在 KVM 中注册的 irqfd 是唯一的，以避免潜在的冲突和错误。补丁包含了13个具体的修改，涉及 irqfd 的初始化、锁的管理、事件队列的处理等多个方面。

本周的讨论中，Sean Christopherson 提到已将该补丁应用于 kvm-x86 的中断请求（irq）处理，并列出了每个补丁的具体链接，显示出补丁的逐步实施情况。这些补丁包括使用本地结构进行初始的 vfs_poll()、在分配过程中获取 SCRU 锁、初始化 irqfd 等待队列回调等，表明该补丁的实施正在顺利进行，且各项功能逐步整合到 KVM 的代码中。

总体来看，本周的进展表明补丁已成功应用，并且各项功能的实现正朝着确保 irqfd 注册唯一性的目标推进。

#### 📝 邮件列表

1. **[06-24 12:38]** Re: [PATCH v3 00/13] KVM: Make irqfd registration globally unique
   - 发件人: Sean Christopherson <seanjc@google.com>

---

### Thread 27: [PATCH] arm64: kvm: trace_handle_exit: use string choices helper

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 24 Jun 2025 06:29:47 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于 ARM64 架构下 KVM 的一个补丁，标题为「[PATCH] arm64: kvm: trace_handle_exit: use string choices helper」。该补丁的主要内容是提议在 `trace_handle_exit` 函数中使用字符串选择助手，以简化代码并提高可读性。

在历史讨论中并没有提供具体的背景信息或之前的讨论内容，邮件列表中仅包含本周的新讨论。

本周的讨论由 Kuninori Morimoto 提出，他在邮件中说明了使用字符串选择助手的必要性，并提交了相关的代码修改。具体来说，补丁对 `trace_handle_exit.h` 文件进行了小幅度的修改，替换了原本的条件表达式（`__entry->is_write ? "write" : "read"`）为调用字符串选择助手的方式（`str_write_read(__entry->is_write)`），从而使代码更加简洁。

总的来说，本周的进展集中在代码优化上，未涉及其他参与者的反馈或进一步的讨论。

#### 📝 邮件列表

1. **[06-24 06:29]** [PATCH] arm64: kvm: trace_handle_exit: use string choices helper
   - 发件人: Kuninori Morimoto <kuninori.morimoto.gx@renesas.com>

---

### Thread 28: [PATCH] arm64: kvm: sys_regs: use string choices helper

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Tue, 24 Jun 2025 06:29:40 +0000

#### 🤖 AI 总结

本邮件讨论的主题是关于对 ARM64 架构下 KVM 的系统寄存器处理代码进行优化的补丁（patch）。该补丁的主要内容是使用字符串选择助手（string choices helper）来简化代码中的读写状态表示，具体体现在 `sys_regs.c` 和 `sys_regs.h` 文件中。

在之前的讨论中，虽然没有具体的历史邮件记录，但可以推测该补丁的提出是为了提高代码的可读性和维护性，减少硬编码字符串的使用。

在本周的新讨论中，Kuninori Morimoto 提出了该补丁，并进行了相应的代码修改，具体包括在两个文件中替换了原有的写入和读取状态的表示方式，使用了 `str_write_read` 函数来代替原来的条件判断。这一修改使得代码更加简洁明了。邮件中附上了修改的代码片段，表明了具体的变更细节。整体来看，本周的讨论集中在补丁的实施及其对代码质量的提升上。

#### 📝 邮件列表

1. **[06-24 06:29]** [PATCH] arm64: kvm: sys_regs: use string choices helper
   - 发件人: Kuninori Morimoto <kuninori.morimoto.gx@renesas.com>

---

## 📌 RFC

共 3 个 thread

---

### Thread 1: [RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Thu, 19 Jun 2025 15:10:15 +0530

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（内核虚拟机）中嵌套虚拟化自测试的补丁（RFC PATCH v2 0/9）。该补丁旨在启用嵌套虚拟化的自测试功能，以便更好地验证虚拟化层的功能。

在历史讨论中，Marc Zyngier 和 Ganapatrao Kulkarni 讨论了嵌套虚拟化的实现细节，特别是如何在不同的虚拟化层（L1、L2、L3）之间切换和运行测试。Ganapatrao 提出，当前的测试需要在主机上启动完整的操作系统，这样的做法显得复杂且不够高效。他强调需要更简单的合成测试，以验证嵌套虚拟化的正确性。

在本周的新讨论中，Ganapatrao 再次强调了自测试的目标是构建一系列简化的虚拟机，而不是依赖于完整的操作系统或复杂的虚拟化环境。Marc Zyngier 对此表示理解，但也指出实现这一目标的复杂性。两位参与者都意识到，尽管目标明确，但实现起来仍然面临挑战。

总结而言，讨论围绕如何有效地实现 KVM 嵌套虚拟化的自测试展开，参与者们在探索简化测试流程的同时，也在面对实现复杂性的问题。

#### 📝 邮件列表

1. **[06-19 15:10]** Re: [RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
2. **[06-19 12:45]** Re: [RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests
   - 发件人: Marc Zyngier <maz@kernel.org>
3. **[06-23 16:01]** Re: [RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests
   - 发件人: Ganapatrao Kulkarni <gankulkarni@os.amperecomputing.com>
4. **[06-23 15:11]** Re: [RFC PATCH v2 0/9] KVM: Enable Nested Virt selftests
   - 发件人: Marc Zyngier <maz@kernel.org>

---

### Thread 2: [RFC PATCH 1/2] KVM: Add arch hooks for KVM syscore ops

**📧 邮件数**: 3 | **👥 参与者**: 1 | **📅 开始时间**: Mon, 23 Jun 2025 14:27:13 +0100

#### 🤖 AI 总结

本邮件线程讨论了两个与 KVM（Kernel-based Virtual Machine）相关的补丁，主要集中在架构钩子和 GIC（通用中断控制器）管理方面。

首先，**第一个补丁**（RFC PATCH 1/2）由 David Woodhouse 提出，目的是为 KVM 的系统核心操作添加架构钩子，允许在 KVM 的关机、挂起和恢复过程中进行架构特定的处理。补丁中新增了 `kvm_arch_shutdown()`、`kvm_arch_suspend()` 和 `kvm_arch_resume()` 函数的弱定义，允许不同架构实现自定义的行为。

**第二个补丁**（RFC PATCH 2/2）同样由 David Woodhouse 提出，解决了在 kexec（内核重启）过程中，因前一个内核的 vLPI（虚拟本地外设中断）挂起表未正确清理而导致的新内核文本损坏的问题。补丁通过在关机时调用 `kvm_vgic_v3_shutdown()` 来解除所有虚拟处理单元（vPE）的映射，确保系统在重启时不会出现数据损坏。

在本周的新讨论中，David Woodhouse 提到之前尝试的一个解决方案未能成功，并分享了在处理 vLPI 挂起表时观察到的特定数据损坏模式。他指出，添加适当的延迟可以解决问题，并强调了在 DMA 设备后面使用 IOMMU 的重要性，以避免此类问题的发生。

总体来看，本周的讨论围绕 KVM 的系统核心操作和 GIC 的管理展开，强调了架构钩子的必要性及其在系统稳定性中的作用。

#### 📝 邮件列表

1. **[06-23 14:27]** [RFC PATCH 1/2] KVM: Add arch hooks for KVM syscore ops
   - 发件人: David Woodhouse <dwmw2@infradead.org>
2. **[06-23 14:27]** [RFC PATCH 2/2] KVM: arm64: vgic-its: Unmap all vPEs on shutdown
   - 发件人: David Woodhouse <dwmw2@infradead.org>
3. **[06-23 18:38]** Re: [RFC PATCH 2/2] KVM: arm64: vgic-its: Unmap all vPEs on shutdown
   - 发件人: David Woodhouse <dwmw2@infradead.org>

---

### Thread 3: [RFC] ARM vGIC-ITS tables serialization when running protected
 VMs

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 26 Jun 2025 08:22:57 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于在运行受保护虚拟机时，ARM vGIC-ITS 表的序列化问题。原始的提案（patch）旨在解决 KVM 在处理虚拟机状态时直接写入来宾内存的问题，而不是将状态传递给用户空间进行序列化，这种做法在没有保密虚拟机的情况下也会导致问题。

在之前的讨论中，David Woodhouse 指出，当来宾虚拟机从休眠状态恢复时，可能会导致 GIC（通用中断控制器）处于错误状态，进而引发内存损坏和虚拟机崩溃。他提到，当前的 KVM 实现并未遵循正常的序列化流程，导致了不必要的复杂性和潜在的错误。

在本周的新讨论中，David Woodhouse 强调了需要一种新的方法，让用户空间能够像处理普通 KVM 设备一样序列化 GIC 状态，避免直接在来宾内存中进行操作。他提到，尽管可能最终会将问题归咎于来宾内核，但现有的实现方式仍需改进，以减少对硬件设计缺陷的依赖。整体来看，本周的讨论推动了对更合理的 GIC 状态管理方案的探索。

#### 📝 邮件列表

1. **[06-26 08:22]** Re: [RFC] ARM vGIC-ITS tables serialization when running protected
 VMs
   - 发件人: David Woodhouse <dwmw2@infradead.org>

---

## 📌 Selftest

共 1 个 thread

---

### Thread 1: kselftest kvm/arm/page_fault_test hangs if pagesize is 16KB

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Fri, 27 Jun 2025 15:34:57 +0900

#### 🤖 AI 总结

本邮件讨论的主题是关于 kselftest 中的 kvm/arm/page_fault_test 测试在使用 16KB 页面大小时出现挂起的问题。

1. **原始问题**：Itaru Kitayama 报告称，在 QEMU TCG 模式下，使用 -cpu max 类型时，kselftest 的 page_fault_test 测试会挂起。邮件中附上了调用栈的详细信息，显示在执行 `arch_local_irq_enable` 函数时发生了挂起。

2. **之前讨论**：本邮件没有提供历史讨论的内容，说明这个问题是首次被提出。

3. **本周进展**：Itaru 进行了测试，发现当页面大小为 4KB 和 64KB 时，page_fault_test 测试能够正常运行。这表明问题可能与 16KB 页面大小的处理有关。

总结来看，当前的讨论集中在 kselftest 测试的挂起问题上，Itaru 提供了详细的调用栈信息，并通过测试确认了问题的特定条件。后续可能需要进一步分析 16KB 页面大小的处理逻辑，以解决该问题。

#### 📝 邮件列表

1. **[06-27 15:34]** kselftest kvm/arm/page_fault_test hangs if pagesize is 16KB
   - 发件人: Itaru Kitayama <itaru.kitayama@linux.dev>

---

## 📌 GIT PULL

共 1 个 thread

---

### Thread 1: [GIT PULL] KVM/arm64 fixes for 6.16, take #4

**📧 邮件数**: 1 | **👥 参与者**: 1 | **📅 开始时间**: Thu, 26 Jun 2025 16:20:23 +0100

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM/arm64 在 6.16 版本中的修复，Marc Zyngier 提交了相关的修复补丁。

**原始 patch/问题的内容**：
本次补丁主要针对 pKVM 的初始化问题，确保在中断控制器不是 GICv3 时，pKVM 能够优雅地失败而不影响主机运行。此外，还修复了在主机 S2 阶段故障时所需的最小 MMIO 范围计算问题，以及在嵌套模式下生成 GICv3 维护中断的错误。

**之前讨论要点**：
由于本邮件没有提供历史讨论的内容，因此无法总结之前的讨论要点。

**本周的新讨论、进展或结论**：
本周的讨论主要集中在提交的补丁上，Marc Zyngier 强调了这组修复并不涉及重大变更，但仍然是必要的改进。具体修复包括：
1. 在中断控制器不是 GICv3 时，优雅地失败初始化 pKVM。
2. 在 carveout 分配失败时，同样优雅地失败初始化 pKVM。
3. 修复主机在阶段 2 故障时的最小 MMIO 范围计算。
4. 修复嵌套模式下 GICv3 维护中断的生成问题。

整体来看，本周的讨论确认了补丁的必要性，并为即将发布的版本做了准备。

#### 📝 邮件列表

1. **[06-26 16:20]** [GIT PULL] KVM/arm64 fixes for 6.16, take #4
   - 发件人: Marc Zyngier <maz@kernel.org>

---

## 📌 Other

共 3 个 thread

---

### Thread 1: [kvm-unit-tests PATCH v4 00/13] arm/arm64: Add kvmtool to the runner script

**📧 邮件数**: 21 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 25 Jun 2025 16:48:00 +0100

#### 🤖 AI 总结

本邮件线程讨论了针对 KVM 单元测试的补丁系列，主要内容是将 kvmtool 添加到测试运行脚本中，以支持 ARM 和 ARM64 架构的测试。

1. **原始补丁/问题内容**：
   该补丁系列的目标是使用户能够通过命令 `./configure --target=kvmtool` 来配置和运行所有测试，利用 kvmtool 作为虚拟化工具。kvmtool 相比于 QEMU 更小、更易于修改，并且在某些情况下运行速度更快。

2. **之前讨论要点**：
   在历史讨论中，参与者们讨论了 kvmtool 的优势和局限性，包括其与 QEMU 的不同之处，以及如何在测试中集成 kvmtool。补丁系列经过多次修改，逐步完善了对 kvmtool 的支持，包括添加必要的参数和环境变量。

3. **本周的新讨论、进展或结论**：
   本周的讨论集中在补丁的具体实现上，包括新增的 `kvmtool_params` 参数、默认参数设置、错误处理等。Alexandru Elisei 提到，虽然 kvmtool 的支持已基本完成，但 EFI 测试仍然不被支持。Andrew Jones 对补丁的多次修改表示认可，并确认已将其应用于 ARM 队列中。最终，补丁系列的目标是使 KVM 单元测试能够在 QEMU 和 kvmtool 下运行，增强了测试的灵活性和可用性。

#### 📝 邮件列表

1. **[06-25 16:48]** [kvm-unit-tests PATCH v4 00/13] arm/arm64: Add kvmtool to the runner script
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[06-25 16:48]** [kvm-unit-tests PATCH v4 01/13] run_tests.sh: Document --probe-maxsmp argument
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
3. **[06-25 16:48]** [kvm-unit-tests PATCH v4 02/13] scripts: Document environment variables
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
4. **[06-25 16:48]** [kvm-unit-tests PATCH v4 03/13] scripts: Refuse to run the tests if not configured for qemu
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
5. **[06-25 16:48]** [kvm-unit-tests PATCH v4 04/13] scripts: Use an associative array for qemu argument names
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
6. **[06-25 16:48]** [kvm-unit-tests PATCH v4 05/13] scripts: Add 'kvmtool_params' to test definition
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
7. **[06-25 16:48]** [kvm-unit-tests PATCH v4 06/13] scripts: Add support for kvmtool
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
8. **[06-25 16:48]** [kvm-unit-tests PATCH v4 07/13] scripts: Add default arguments for kvmtool
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
9. **[06-25 16:48]** [kvm-unit-tests PATCH v4 08/13] scripts: Add KVMTOOL environment variable for kvmtool binary path
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
10. **[06-25 16:48]** [kvm-unit-tests PATCH v4 09/13] scripts: Detect kvmtool failure in premature_failure()
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
11. **[06-25 16:48]** [kvm-unit-tests PATCH v4 10/13] scripts: Do not probe for maximum number of VCPUs when using kvmtool
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
12. **[06-25 16:48]** [kvm-unit-tests PATCH v4 11/13] scripts/mkstandalone: Export $TARGET
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
13. **[06-25 16:48]** [kvm-unit-tests PATCH v4 12/13] scripts: Add 'disabled_if' test definition parameter for kvmtool to use
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
14. **[06-25 16:48]** [kvm-unit-tests PATCH v4 13/13] scripts: Enable kvmtool
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
15. **[06-26 17:25]** Re: [kvm-unit-tests PATCH v4 03/13] scripts: Refuse to run the tests
 if not configured for qemu
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
16. **[06-26 17:29]** Re: [kvm-unit-tests PATCH v4 04/13] scripts: Use an associative
 array for qemu argument names
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
17. **[06-26 17:34]** Re: [kvm-unit-tests PATCH v4 05/13] scripts: Add 'kvmtool_params' to
 test definition
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
18. **[06-26 17:43]** Re: [kvm-unit-tests PATCH v4 07/13] scripts: Add default arguments
 for kvmtool
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
19. **[06-26 17:41]** Re: [kvm-unit-tests PATCH v4 05/13] scripts: Add 'kvmtool_params' to
 test definition
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
20. **[06-26 18:42]** Re: [kvm-unit-tests PATCH v4 00/13] arm/arm64: Add kvmtool to the
 runner script
   - 发件人: Andrew Jones <andrew.jones@linux.dev>
21. **[06-26 17:48]** Re: [kvm-unit-tests PATCH v4 00/13] arm/arm64: Add kvmtool to the
 runner script
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>

---

### Thread 2: [kvm-unit-tests PATCH 0/2] scripts: extra_params rework

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Wed, 25 Jun 2025 16:43:52 +0100

#### 🤖 AI 总结

本邮件讨论的主题是对 KVM 单元测试脚本中 `extra_params` 的重构，主要涉及两个补丁。

**原始问题/补丁内容**：
补丁的目的是为了引入 `kvmtool_params`，以支持在 ARM 和 ARM64 架构上使用 kvmtool 运行测试。为此，`extra_params` 被重命名为 `qemu_params`，以便清晰区分 QEMU 和 kvmtool 的命令行选项，同时保留 `extra_params` 以兼容用户自定义的测试定义。

**之前讨论要点**：
在之前的讨论中，参与者指出了 kvmtool 和 QEMU 在运行虚拟机时的语法差异，并强调了需要通过新的参数来解决这一问题。`extra_params` 被认为不够明确，因此决定进行重命名和重构。

**本周新讨论及进展**：
本周的讨论中，Alexandru Elisei 提出了两个补丁：
1. 将 `extra_params` 重命名为 `qemu_params`，并保持兼容性。
2. 引入新的测试定义参数 `test_args`，用于传递与虚拟机管理程序无关的参数，以便于未来在 kvmtool 支持下使用。

这些补丁已获得 Andrew Jones 的认可，并鼓励其他架构维护者也进行确认。整体上，讨论集中在提高代码的清晰度和可维护性上。

#### 📝 邮件列表

1. **[06-25 16:43]** [kvm-unit-tests PATCH 0/2] scripts: extra_params rework
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
2. **[06-25 16:43]** [kvm-unit-tests PATCH 1/2] scripts: unittests.cfg: Rename 'extra_params' to 'qemu_params'
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
3. **[06-25 16:43]** [kvm-unit-tests PATCH 2/2] scripts: Add 'test_args' test definition parameter
   - 发件人: Alexandru Elisei <alexandru.elisei@arm.com>
4. **[06-26 16:58]** Re: [kvm-unit-tests PATCH 0/2] scripts: extra_params rework
   - 发件人: Andrew Jones <andrew.jones@linux.dev>

---

### Thread 3: KVM: arm64: vgic-its: Return -ENXIO to invalid
 KVM_DEV_ARM_VGIC_GRP_CTRL attrs

**📧 邮件数**: 4 | **👥 参与者**: 2 | **📅 开始时间**: Mon, 23 Jun 2025 15:22:52 +0200

#### 🤖 AI 总结

本邮件讨论的主题是关于 KVM（Kernel-based Virtual Machine）在 arm64 架构下的 vgic-its 组件中，针对无效的 KVM_DEV_ARM_VGIC_GRP_CTRL 属性返回 -ENXIO 错误码的补丁。

在历史讨论中，未有相关的补丁或讨论记录。本周的讨论主要围绕 David Woodhouse 提出的补丁，补丁内容是在 vgic-its.c 文件中添加了对无效属性返回 -ENXIO 的处理，以便更好地反映设备状态。补丁的初步版本尝试通过 ioctl 调用 unmap_all_vpes() 函数，但由于使用了错误的文件描述符而未能成功。

在本周的讨论中，Eric Auger 提出补丁中的错误码与文档中描述的情况不完全匹配，建议更新文档或更改返回值。David Woodhouse 则回应称，-ENXIO 的返回值已在 KVM 的高层描述中涵盖，因此不需要更改。最终，Eric Auger 表示对补丁进行了审核，并认为这不是大问题。

总结来看，本周的讨论主要集中在补丁的合理性及其与文档的一致性上，最终得到了 Eric 的认可。

#### 📝 邮件列表

1. **[06-23 15:22]** KVM: arm64: vgic-its: Return -ENXIO to invalid
 KVM_DEV_ARM_VGIC_GRP_CTRL attrs
   - 发件人: David Woodhouse <dwmw2@infradead.org>
2. **[06-24 09:25]** Re: KVM: arm64: vgic-its: Return -ENXIO to invalid
 KVM_DEV_ARM_VGIC_GRP_CTRL attrs
   - 发件人: Eric Auger <eauger@redhat.com>
3. **[06-24 11:01]** Re: KVM: arm64: vgic-its: Return -ENXIO to invalid
 KVM_DEV_ARM_VGIC_GRP_CTRL attrs
   - 发件人: David Woodhouse <dwmw2@infradead.org>
4. **[06-24 11:20]** Re: KVM: arm64: vgic-its: Return -ENXIO to invalid
 KVM_DEV_ARM_VGIC_GRP_CTRL attrs
   - 发件人: Eric Auger <eauger@redhat.com>

---

